subroutine usage(routine_name)

    implicit none

    character(len=*), intent(in) :: routine_name

    write(*,'(3A)') 'usage: python ', routine_name, &
                    ' [-d | --debug]'// &
                    ' [-h | --help]'// &
                    ' [(-i | --input) INPUT_FILE_NAME]'// &
                    ' [(-o | --output) OUTPUT_FILE_NAME]'

end subroutine usage


subroutine parse_args()

    use imc_global_io_data,   only: input_file, output_file

    implicit none

    character(len=256) :: routine_name
    logical            :: print_help
    logical            :: debug_mode

    character(len=256) :: cmdline_arg
    integer(kind=4)    :: cmdline_len
    integer(kind=4)    :: cmdline_stat
    integer(kind=4)    :: iarg

    input_file = 'fcimc.in'
    output_file = 'fcimc.out'
    print_help = .false.
    debug_mode = .false.

    ! Fortran 2003 standard (get_command_argument)...
    iarg = 1
    do
        call get_command_argument(iarg, cmdline_arg, cmdline_len, cmdline_stat)
        if (cmdline_stat > 0) exit

        select case (trim(cmdline_arg))
        case ('-i', '--input')
            iarg = iarg + 1
            call get_command_argument(iarg, cmdline_arg, cmdline_len, cmdline_stat)
            if (cmdline_stat /= 0) then
                write(*,*) 'Error reading input file name'
                stop
            endif
            input_file = trim(cmdline_arg)
        case ('-o', '--output')
            iarg = iarg + 1
            call get_command_argument(iarg, cmdline_arg, cmdline_len, cmdline_stat)
            if (cmdline_stat /= 0) then
                write(*,*) 'Error reading output file name'
                stop
            endif
            output_file = trim(cmdline_arg)
        case ('-h', '--help')
            print_help = .true.
        case ('-d', '--debug')
            debug_mode = .true.
        case default
            write(*,*) 'Unrecognised command line option: ', trim(cmdline_arg)
            stop
        end select
        iarg = iarg + 1
    enddo

    if (print_help) then
      call get_command_argument(0, routine_name)
      call usage(trim(routine_name))
      stop
    endif

end subroutine parse_args


program main
    ! Top-level main program for fcimc.
    use imc_global_part_data, only: n_max, xpos, icell, nrg, startnrg, dead, &
                                    t, mu, frq, origin, inext
    use imc_utils,            only: init_random_seed

    implicit none

    integer       :: tcom, tfin, clock_rate
    integer       :: rng_seed

    call system_clock(tcom)

    call parse_args()

    rng_seed = 12345
    call init_random_seed(rng_seed) ! Non-zero argument fixes random number sequence - reproducible

    n_max = 20000

    call imc_user_input_read
    call imc_user_input_echo

    allocate(origin(n_max))
    allocate(xpos(n_max))
    allocate(t(n_max))
    allocate(mu(n_max))
    allocate(nrg(n_max))
    allocate(startnrg(n_max))
    allocate(frq(n_max))
    allocate(icell(n_max))
    allocate(dead(n_max))
    origin(:)   = 0
    xpos(:)     = 0.d0
    t(:)        = 0.d0
    mu(:)       = 0.d0
    nrg(:)      = 0.d0
    startnrg(:) = 0.d0
    frq(:)      = 0.d0
    icell(:)    = 0
    dead(:)     = .true.
    inext       = 1

    call imc_mesh_make

    call imc_opcon

    deallocate(origin)
    deallocate(xpos)
    deallocate(t)
    deallocate(mu)
    deallocate(nrg)
    deallocate(startnrg)
    deallocate(frq)
    deallocate(icell)
    deallocate(dead)

    call system_clock(tfin, clock_rate)
    write(*,'(A,F10.2,A)') 'Time taken for simulation = ', &
        & float(tfin - tcom) / float(clock_rate), ' s'

end program main
