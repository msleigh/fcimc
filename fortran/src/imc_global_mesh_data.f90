module imc_global_mesh_data

    implicit none

    real(kind=8) :: xsize  = -1.d0
    real(kind=8) :: dx     = -1.d0
    integer      :: ncells = -1

    real(kind=8), allocatable, dimension(:) :: cellpos
    real(kind=8), allocatable, dimension(:) :: nodepos
    real(kind=8), allocatable, dimension(:) :: sigma_p
    real(kind=8), allocatable, dimension(:) :: temp
    real(kind=8), allocatable, dimension(:) :: temp0
    real(kind=8), allocatable, dimension(:) :: beta
    real(kind=8), allocatable, dimension(:) :: fleck
    real(kind=8), allocatable, dimension(:) :: nrgdep

end module imc_global_mesh_data
