module imc_global_part_data

implicit none


! Number of particles stored in the census
integer(kind=8) :: n_census = -1

! Total number of particles permitted in the calculation at any time
integer(kind=8) :: n_max = -1

! Number of particles added per timestep
integer(kind=8) :: n_input = -1

real(kind=8), allocatable, dimension(:) :: t
real(kind=8), allocatable, dimension(:) :: xpos
real(kind=8), allocatable, dimension(:) :: mu
real(kind=8), allocatable, dimension(:) :: frq
real(kind=8), allocatable, dimension(:) :: nrg
real(kind=8), allocatable, dimension(:) :: startnrg
integer, allocatable, dimension(:)      :: origin
integer, allocatable, dimension(:)      :: icell
logical, allocatable, dimension(:)      :: dead

integer(kind=8) :: inext

end module imc_global_part_data
