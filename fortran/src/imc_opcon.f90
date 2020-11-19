subroutine imc_opcon

    use imc_global_io_data,   only: output_file
    use imc_global_mesh_data, only: temp0, temp, cellpos
    use imc_global_phys_data, only: c
    use imc_global_time_data, only: time, ns, step, dt

    use imc_utils,            only: imc_get_free_lun

    implicit none

    real(kind=8), dimension(3) :: plottimes = (/ 6.d0, 15.d0, 90.d0 /)
    integer                    :: plottimenext = 1
    integer                    :: fname

    ! Open output file
    fname = imc_get_free_lun()
    open(unit=fname, file=output_file, action='write', form='formatted', status='unknown')

    ! Set an initial temperature field
    temp(:) = temp0(:)  ! keV

    ! Loop over timesteps

    time = 0.d0

    do step = 0, ns - 1

        write(*,'(/,A)')      "==============================================================================="
        write(*,'(A,I4)')     'Timestep  ', step
        write(*,'(A,ES24.16)') 'Time (s)  ', time
        write(*,'(A,ES24.16)') 'Time (cm) ', (time * c)
        write(*,'(A)')        "==============================================================================="

        ! Update temperature-dependent quantities
        call imc_update

        ! Source new particles
        call imc_source

        ! Track new particles through the mesh
        call imc_track

        ! Tally
        call imc_tally

        ! Energy check
        !

        ! Update time
        time = time + dt

        ! Plot
        if (plottimenext <= 3) then
            if ((time * c + 1.d-06) >= plottimes(plottimenext)) then
                write(*,'(A,I6)')     'Plotting ', plottimenext
                write(*,'(A,F24.16)') 'at target time ', plottimes(plottimenext)
                write(*,'(A,F24.16)') 'at actual time ', (time * c)
                write(fname,'(A,F24.16)') 'Time = ',time * c
                write(fname,*) cellpos(:)
                write(fname,*) temp(:)
                plottimenext = plottimenext + 1
            endif
        endif

    enddo

    ! Close output file
    close(fname)

end subroutine imc_opcon
