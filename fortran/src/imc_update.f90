subroutine imc_update

    use imc_global_bcon_data, only: t0
    use imc_global_mat_data,  only: gamma, bee
    use imc_global_mesh_data, only: sigma_p, temp, beta, fleck, xsize, temp0, dx
    use imc_global_phys_data, only: x15pi4, pi, c, h, a
    use imc_global_time_data, only: step, dt

    implicit none

    write(*,'(/,A)')    '-------------------------------------------------------------------------------'
    write(*,'(A,I4,A)') 'Update step (',step,')'
    write(*,'(A)')      '-------------------------------------------------------------------------------'

    ! Calculate Planck mean opacity for the mesh
    ! ------------------------------------------

    ! In general do this every time-step because sigma can be temperature-dependent
    ! There is a factor gamma missing that is problem-dependent (assumed = 1 here)

    sigma_p(:) = x15pi4 * gamma * temp(:)**(-3)

    write(*,'(/,A)') 'Planck mean opacity (Fleck & Cummings 1971 Eqn 4.7)'
    write(*,'(4(ES16.8,1X))') 8.d0 * pi * gamma / (c**3 * h**3 * a * temp(:)**3)
    write(*,'(A)') 'Planck mean opacity (Wollaber 2008 Eqn 2.21)'
    write(*,'(4(ES16.8,1X))') sigma_p(:)
    write(*,'(A)') '...These should match...'
    write(*,'(A)') '...These should decrease as T^3...'

    ! Calculate beta for the mesh
    ! ---------------------------

    beta(:) = 4.d0 * a * (temp(:)**3) / bee

    write(*,'(/,A)') 'Beta (non-linearity factor) (Fleck & Cummings 1971 Eqn 1.6)'
    write(*,'(4(ES16.8,1X))') beta
    write(*,'(A)') '...This should increase as T^3...'

    ! Fleck
    ! -----

    fleck(:) = 1.d0 / (1.d0 + beta(:) * c * dt * sigma_p(:))

    write(*,'(/,A)') 'Fleck factor (Fleck & Cummings 1971 Eqn 4.1d)'
    write(*,'(10(F6.3,1X))') fleck
    write(*,'(A)') '...This should be constant (for a given timestep length)...'
    write(*,'(A,F10.8,A)') '...This should equal ', &
        (1.d0 / (1.d0 + (32.d0 * pi * gamma / (c**3 * h**3 * bee)) * c * dt)), &
        '...'
    write(*,'(/,A,F6.3, A)') 'Slab thickness       = ', xsize, ' cm'
    write(*,'(A,F6.3, A)') 'Boundary source temp = ', t0, ' keV'
    write(*,'(A,F6.3)') 'Material gamma/D     = ', gamma
    write(*,'(A,F6.3, A)') 'Sigma at nu = 3 keV  = ', gamma / (3.d0**3), ' cm^-1'
    !write(*,'(A,F6.3)') 'Sigma at nu = 3 keV  = ', &
    !    & gamma * (1.d0 - exp(-3. / 0.001)) / (3.d0**3), ' cm^-1'
    write(*,'(A,F6.3)') 'Spatial step         = ', dx
    write(*,'(A,F6.3, A)') 'Time step            = ', (dt / 1.d-08), ' sh'
    write(*,'(/,A)') 'Initial temperature (keV):'
    write(*,'(10(F6.3,1X))') temp0
    write(*,'(/,A)') 'Scattering fraction (%):'
    write(*,'(10(F4.1,1X))') 100.d0 * (1.d0 - fleck(:))

end subroutine imc_update
