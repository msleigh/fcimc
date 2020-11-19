subroutine imc_get_energy_sources(e_surf, e_body, e_total)

    use imc_global_mesh_data, only: ncells, fleck, sigma_p, temp, dx
    use imc_global_bcon_data, only: t0
    use imc_global_phys_data, only: sb, a, c
    use imc_global_time_data, only: dt

    implicit none

    real(kind=8), intent(out)                    :: e_surf
    real(kind=8), intent(out)                    :: e_total
    real(kind=8), dimension(ncells), intent(out) :: e_body

    ! Left-hand boundary is a black-body emitter at constant temperature T0
    ! (Energy radiated per unit area = sigma.T0**4 (sigma = S-B constant)
    e_surf = sb * t0**4 * dt

    ! Emission source term
    e_body(:) = (fleck(:) * sigma_p(:) * a * c * temp(:)**4 * dx * dt)

    ! Total energy emitted
    e_total = e_surf + sum(e_body(:))

    write(*,'(/,A)') 'Energy radiated in timestep:'
    write(*,'(/,A)') 'In total:'
    write(*,'(ES24.16)') e_total
    write(*,'(/,A)') 'By boundary condition:'
    write(*,'(ES24.16)') e_surf
    write(*,'(/,A)') 'By mesh:'
    write(*,'(4(ES16.8))') e_body

end subroutine imc_get_energy_sources


subroutine imc_get_emission_probabilities(e_surf, e_body, e_total, p_surf, p_body)

    use imc_global_mesh_data, only: ncells

    implicit none

    real(kind=8), intent(in)                       :: e_surf
    real(kind=8), intent(in)                       :: e_total
    real(kind=8), dimension(ncells), intent(in)    :: e_body
    real(kind=8), intent(out)                      :: p_surf
    real(kind=8), dimension(0:ncells), intent(out) :: p_body
    integer                                        :: jcell

    p_surf = e_surf / e_total

    ! Probability of each cell given that the particle is from the mesh not the surface

    p_body(0) = 0.d0
    do jcell = 1, ncells
      p_body(jcell) = p_body(jcell-1) + e_body(jcell) / sum(e_body(:))
    enddo

    write(*,'(A)')
    write(*,'(A)') 'Probabilities:'
    write(*,'(A)')
    write(*,'(A)') 'In total'
    write(*,'(ES16.8)') p_surf + sum(p_body(:))
    write(*,'(A)')
    write(*,'(A)') 'Of boundary particle'
    write(*,'(ES16.8)') p_surf
    write(*,'(A)')
    write(*,'(A)') 'Of mesh particle (cumulative)'
    write(*,'(10F4.1)') p_body(1:ncells)

end subroutine imc_get_emission_probabilities


subroutine imc_get_source_particle_numbers(p_surf, p_body, n_surf, n_body)

    !use imc_global_bcon_data, only: t0
    use imc_global_mesh_data, only: ncells !, dx, temp, nodepos
    use imc_global_part_data, only: n_max, n_census, n_input !, , dead, xpos, icell, mu, &
    !                              & frq, nrg, startnrg, t, origin, inext
    !use imc_global_phys_data, only: h
    !use imc_global_time_data, only: step, dt, time
    !use imc_utils,            only: samplePlanckspectrum

    implicit none

    real(kind=8), intent(in)                        :: p_surf
    real(kind=8), dimension(0:ncells), intent(in)   :: p_body
    integer(kind=8), intent(out)                    :: n_surf
    integer(kind=8), dimension(ncells), intent(out) :: n_body
    real(kind=8)                            :: eta
    integer(kind=8)                         :: ip
    integer(kind=8)                         :: irannum
    integer(kind=8)                         :: n_source
    real(kind=8), allocatable, dimension(:) :: r
    integer                                 :: jcell

    ! Determine total number of particles to source this time-step
    n_source = n_input
    if ((n_source + n_census) > n_max) &
        n_source = n_max - n_census - ncells - 1

    write(*,'(/,A,I8,A)') 'Sourcing ',n_source,' particles this timestep'
    write(*,'(A,I8,A)') '(User requested ',n_input,' per timestep)'

    n_surf    = 0
    n_body(:) = 0

    allocate(r(2*n_source))
    call random_number(r)
    irannum = 0

    ! Calculate the number of particles emitted by the surface source and each mesh cell
    do ip = 1, n_source
        irannum = irannum + 1
        if (r(irannum) <= p_surf) then
            n_surf = n_surf + 1
        else
            irannum = irannum + 1
            eta = r(irannum)
            do jcell = 1, ncells
                if (eta <= p_body(jcell)) then
                    n_body(jcell) = n_body(jcell) + 1
                    exit
                endif
            enddo
        endif
    enddo
    deallocate(r)

    write(*,'(/,A)') 'Body source'
    write(*,'(10I6)') n_body(:)

end subroutine imc_get_source_particle_numbers


subroutine imc_source_particles(e_surf, e_body, n_surf, n_body)

    use imc_global_bcon_data, only: t0
    use imc_global_mesh_data, only: ncells, dx, temp, nodepos
    use imc_global_part_data, only: icell, inext, n_max, nrg, startnrg, dead, xpos, icell, mu, &
                                  & frq, nrg, startnrg, t, origin, inext
    use imc_global_phys_data, only: h
    use imc_global_time_data, only: dt, time ! step, dt, time
    use imc_utils,            only: samplePlanckspectrum

    implicit none

    real(kind=8), intent(in)                       :: e_surf
    real(kind=8), dimension(ncells), intent(in)    :: e_body
    integer(kind=8), intent(in)                    :: n_surf
    integer(kind=8), dimension(ncells), intent(in) :: n_body
    integer(kind=8)                         :: ip
    integer(kind=8)                         :: irannum
    real(kind=8), allocatable, dimension(:) :: r
    integer                                 :: jcell
    real(kind=8)                            :: jnrg
    real(kind=8)                            :: jstartnrg

    allocate(r(2*n_surf + 4*sum(n_body(:))))
    call random_number(r)
    irannum = 0

    ! Create the surface-source particles
    jnrg = e_surf/real(n_surf, 8)
    jstartnrg = jnrg
    do ip = 1, n_surf
        do while (.not. dead(inext))
           inext = inext + 1
           if (inext > n_max) inext = 1
        enddo
        dead(inext)     = .false.
        origin(inext)   = -1
        xpos(inext)     = 0.d0
        irannum         = irannum + 1
        t(inext)        = time + r(irannum) * dt
        irannum         = irannum + 1
        mu(inext)       = sqrt(r(irannum))                    ! Corresponds to f(mu) = 2mu
        frq(inext)      = t0 * samplePlanckspectrum() / h
        icell(inext)    = 1
        nrg(inext)      = jnrg
        startnrg(inext) = jstartnrg
    enddo

    ! Create the body-source particles
    do jcell = 1, ncells
        if (n_body(jcell) <= 0) &
            cycle
        jnrg = e_body(jcell)/real(n_body(jcell), 8)
        jstartnrg = jnrg
        do ip = 1, n_body(jcell)
            do while (.not. dead(inext))
                inext = inext + 1
                if (inext > n_max) inext = 1
            enddo
            dead(inext)     = .false.
            origin(inext)   = jcell
            irannum         = irannum + 1
            xpos(inext)     = nodepos(jcell) + r(irannum) * dx
            irannum         = irannum + 1
            mu(inext)       = 1.d0 - 2.d0 * r(irannum)
            irannum         = irannum + 1
            t(inext)        = time + r(irannum) * dt
            irannum         = irannum + 1
            frq(inext)      = temp(jcell) * abs(log(r(irannum))) / h
            icell(inext)    = jcell
            nrg(inext)      = jnrg
            startnrg(inext) = jstartnrg
        enddo
    enddo

    deallocate(r)

end subroutine imc_source_particles


subroutine imc_source

    use imc_global_mesh_data, only: ncells
    use imc_global_part_data, only: n_max, dead
    use imc_global_phys_data, only: h
    use imc_global_time_data, only: step

    implicit none

    real(kind=8)                            :: e_surf
    real(kind=8)                            :: e_total
    real(kind=8), dimension(ncells)         :: e_body
    real(kind=8)                            :: p_surf
    real(kind=8), dimension(0:ncells)       :: p_body
    integer(kind=8)                         :: n_surf
    integer(kind=8), dimension(ncells)      :: n_body
    integer(kind=8)                         :: numparts
    integer(kind=8)                         :: ip

    write(*,'(/,A)')    '-------------------------------------------------------------------------------'
    write(*,'(A,I4,A)') 'Source step (',step,')'
    write(*,'(A)')      '-------------------------------------------------------------------------------'

    ! Determine probability of particles belonging to sources
    ! -------------------------------------------------------

    ! Get the energy source terms
    call imc_get_energy_sources(e_surf, e_body, e_total)

    ! Emission probabilities
    call imc_get_emission_probabilities(e_surf, e_body, e_total, p_surf, p_body)

    ! Number of source particles
    call imc_get_source_particle_numbers(p_surf, p_body, n_surf, n_body)

    ! Create the particles
    call imc_source_particles(e_surf, e_body, n_surf, n_body)

    ! Particle count
    numparts = 0
    do ip = 1, n_max
        if (.not. dead(ip)) numparts = numparts + 1
    enddo
    write(*,'(A,I12)') 'Number of particles in the system = ', numparts

end subroutine imc_source
