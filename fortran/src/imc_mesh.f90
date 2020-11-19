subroutine imc_mesh_make

    use imc_global_mat_data,  only: tmp0
    use imc_global_mesh_data, only: dx, xsize, ncells, cellpos, nodepos, temp, temp0, sigma_p, &
                                    beta, fleck, nrgdep

    implicit none

    integer :: icell

    dx = xsize / float(ncells)

    allocate(cellpos(ncells))
    allocate(nodepos(ncells + 1))

    do icell = 1, ncells
        cellpos(icell) = (icell - 0.5d0) * dx
        nodepos(icell) = (icell - 1)     * dx
    enddo
    nodepos(ncells + 1) = ncells * dx

    allocate(temp(ncells))      ! Temperature (keV)
    allocate(temp0(ncells))     ! Initial temperature (keV)
    allocate(sigma_p(ncells))   ! Opacity
    allocate(beta(ncells))      ! Beta factor
    allocate(fleck(ncells))     ! Fleck factor
    allocate(nrgdep(ncells))    ! Total energy deposited in timestep

    temp(:)    = -1.d0
    temp0(:)   = -1.d0
    sigma_p(:) = -1.d0
    beta(:)    = -1.d0
    fleck(:)   = -1.d0
    nrgdep(:)  = -1.d0

    temp0(:) = tmp0


end subroutine imc_mesh_make
