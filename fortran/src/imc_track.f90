subroutine imc_track

    use imc_global_mat_data,  only: gamma, tpower
    use imc_global_mesh_data, only: ncells, nrgdep, temp, nodepos, fleck
    use imc_global_part_data, only: n_census, n_max, dead, frq, icell, mu, xpos, &
                                    nrg, startnrg, t
    use imc_global_phys_data, only: invh3, h, c, invc, invh
    use imc_global_time_data, only: step, time, dt

    implicit none

    real(kind=8) :: endsteptime
    integer(kind=8) :: iptcl, irannum, numparts
    real(kind=8), allocatable, dimension(:) :: r
    real(kind=8) :: sigma, dist_b, dist_col, dist_cen, dist, flecksig, newnrg, startnrg_loc

    write(*,'(/,A)') '-------------------------------------------------------------------------------'
    write(*,'(A,I4,A)') 'Tracking step (',step,')'
    write(*,'(A)')   '-------------------------------------------------------------------------------'


    ! Create local storage for the energy deposited this timestep
    nrgdep(:) = 0.d0

    n_census = 0

    endsteptime = time + dt

    write(*,'(/,A)') 'Particle loop...'

    allocate(r(20*n_max))
    call random_number(r)
    irannum = 0

    ! Loop over all particles
    do iptcl = 1, n_max

        if (dead(iptcl)) cycle

        startnrg_loc = 0.01d0 * startnrg(iptcl)

        ! Loop over segments in the history (between boundary-crossings and collisions)
        do

            ! Calculate the total macroscopic cross-section (cm^-1)
            sigma = ( &
                gamma * invh3 &
                * (1.d0 - exp(-h * frq(iptcl) / temp(icell(iptcl)))) &
                / (frq(iptcl) ** 3 * temp(icell(iptcl)) ** tpower) &
            )

            flecksig = -fleck(icell(iptcl)) * sigma

            ! Distance to boundary
            if (mu(iptcl) > 0.d0) then
                dist_b = (nodepos(icell(iptcl) + 1) - xpos(iptcl)) / mu(iptcl)
            else
                dist_b = (nodepos(icell(iptcl)) - xpos(iptcl)) / mu(iptcl)
            endif

            ! Distance to collision
            if (irannum == 20*n_max) then
                call random_number(r)
                irannum = 1
            else
                irannum = irannum + 1
            endif
            dist_col = abs(log(r(irannum))) / (sigma + flecksig)

            ! Distance to census
            dist_cen = c * (endsteptime - t(iptcl))

            ! Actual distance - whichever happens first
            dist = min(dist_b, dist_col, dist_cen)

            ! Calculate the new energy and the energy deposited (temp storage)
            newnrg = nrg(iptcl) * exp(flecksig * dist)
            if (newnrg <= startnrg_loc) &
                newnrg = 0.d0

            ! Deposit the particle's energy
            nrgdep(icell(iptcl)) = nrgdep(icell(iptcl)) + (nrg(iptcl) - newnrg)

            if (newnrg == 0.d0) then
                dead(iptcl) = .true.
                exit
            endif

            ! If the event was a boundary-crossing, and the boundary is the
            ! domain boundary, then kill the particle
            if (dist == dist_b) then
                if (mu(iptcl) > 0.d0) then
                    if (icell(iptcl) == ncells) then
                        dead(iptcl) = .true.
                        exit
                    endif
                    icell(iptcl) = icell(iptcl) + 1
                elseif (mu(iptcl) < 0.d0) then
                    if (icell(iptcl) == 1) then
                        dead(iptcl) = .true.
                        exit
                    endif
                    icell(iptcl) = icell(iptcl) - 1
                endif
            endif

            ! Otherwise, advance the position, time and energy
            xpos(iptcl) = xpos(iptcl) + mu(iptcl) * dist
            t(iptcl) = t(iptcl) + dist * invc
            nrg(iptcl) = newnrg

            ! If the event was census, finish this history
            if (dist == dist_cen) then
                ! Finished with this particle
                n_census = n_census + 1
                exit
            endif

            ! If event was collision, also update frequency and direction
            if (dist == dist_col) then
                ! Collision (i.e. absorption, but treated as pseudo-scattering)
                if (irannum == 20*n_max) then
                    call random_number(r)
                    irannum = 1
                else
                    irannum = irannum + 1
                endif
                frq(iptcl) = temp(icell(iptcl)) * abs(log(r(irannum))) * invh
                if (irannum == 20*n_max) then
                    call random_number(r)
                    irannum = 1
                else
                    irannum = irannum + 1
                endif
                mu(iptcl)  = 1.d0 - 2.d0 * r(irannum)
            endif

        enddo  ! End loop over history segments

    enddo  ! End loop over history segments

    deallocate(r)

    numparts = 0
    do iptcl = 1, n_max
        if (.not. dead(iptcl)) numparts = numparts + 1
    enddo
    write(*,'(/,A,I16)') 'Number of particles in the system = ', numparts

end subroutine imc_track
