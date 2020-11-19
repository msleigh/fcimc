module imc_global_phys_data

implicit none

real(kind=8), parameter :: c  = 3.d10
real(kind=8), parameter :: pi = 3.14159265359d0
real(kind=8), parameter :: h  = 4.1356675d-18                   ! KeV.s
real(kind=8), parameter :: sb = 2. * pi**5 / (15. * h**3*c**2)  ! keV^-3.cm^-2.s^-1 (flux-like)
real(kind=8), parameter :: a  = 4.d0 * sb / c

real(kind=8), parameter :: invc   = 1. / c
real(kind=8), parameter :: invh   = 1. / h
real(kind=8), parameter :: invh3  = 1. / h**3
real(kind=8), parameter :: x15pi4 = 15. / pi**4

end module imc_global_phys_data
