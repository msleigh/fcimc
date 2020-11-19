module imc_utils

implicit none

contains

integer(kind=4) function imc_get_free_lun()

    integer :: ilun
    logical :: isopen

    isopen = .true.
    ilun   = -1

    do while (isopen)
        ilun = ilun + 1
        inquire(unit=ilun, opened=isopen)
    enddo

    imc_get_free_lun = ilun

end function imc_get_free_lun


subroutine init_random_seed(seed1)

    ! Seed the random number generator.
    ! If seed1 = 0 then set seed1 randomly using the system clock.
    !              This will give different sequences of random numbers
    !              from different runs, so results are not reproducible.
    ! If seed1 > 0 then results will be reproducible since calling this
    !              twice with the same seed will initialize the random
    !              number generator so the same sequence is generated.
    ! Once seed1 is set, set the other elements of the seed array by adding
    ! multiples of 37 as suggested in the documentation.
    ! The length of the seed array is determined by calling
    !
    integer, intent(inout) :: seed1

    integer :: nseed, clock, i
    integer, dimension(:), allocatable :: seed

    call random_seed(size = nseed)  ! determine how many numbers needed to seed
    allocate(seed(nseed))

    if (seed1 == 0) then
        ! randomize the seed: not repeatable
        call system_clock(count = clock)
        seed1 = clock
      endif

    do i=1,nseed
        seed(i) = seed1 + 37*(i-1)
        enddo

    call random_seed(put = seed)   ! seed the generator
    deallocate(seed)

end subroutine init_random_seed


real(kind=8) function samplePlanckspectrum()

    use imc_global_phys_data, only: pi

    real(kind=8) :: r1, r2, r3, r4, n, tmpsum, x
    real(kind=8), dimension(4) :: r
    n = 1.d0
    call random_number(r1)
    tmpsum = 1.d0
    do
        if (r1 <= 90.d0 * tmpsum / pi**4) then
            call random_number(r)
            r1 = r(1)
            r2 = r(2)
            r3 = r(3)
            r4 = r(4)
            x = -log(r1 * r2 * r3 * r4) / n
            exit
        endif
        n = n + 1.d0
        tmpsum = tmpsum + 1.d0 / n**4
    enddo

    samplePlanckspectrum = x

end function samplePlanckspectrum


end module imc_utils
