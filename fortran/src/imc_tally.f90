subroutine imc_tally()

    use imc_global_mat_data,  only: bee
    use imc_global_mesh_data, only: ncells, dx, temp, fleck, sigma_p, nrgdep
    use imc_global_phys_data, only: c, a
    use imc_global_time_data, only: step, dt

    implicit none

    real(kind=8), dimension(ncells) :: radnrgdens
    real(kind=8), dimension(ncells) :: nrg_inc

    write(*,'(/,A)')    '-------------------------------------------------------------------------------'
    write(*,'(A,I4,A)') 'Tally step (',step,')'
    write(*,'(A)')      '-------------------------------------------------------------------------------'

    ! Start-of-step radiation energy density
    radnrgdens(:) = a * temp(:)**4

    ! Temperature increase
    nrg_inc(:)  = ( &
        nrgdep(:) / dx &
        - fleck(:) * c * dt * sigma_p(:) * radnrgdens(:) &
    )

    temp(:) = temp(:) + nrg_inc(:) / bee

    write(*,'(/,A)') 'Mesh temperature:'
    write(*,'(4(ES16.8))') temp

end subroutine imc_tally
