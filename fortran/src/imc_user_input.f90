subroutine to_lower(word)

  ! convert a word to lower case

  character (len=*) , intent(inout) :: word
  integer                           :: i,ic,nlen

  nlen = len(word)

  do i=1,nlen
      ic = iachar(word(i:i))
      if (ic >= 65 .and. ic <= 90) word(i:i) = achar(ic+32)
  end do

end subroutine to_lower


subroutine imc_user_input_read(input_file)

    use imc_utils,            only: imc_get_free_lun
    use imc_global_time_data, only: dt, ns
    use imc_global_mesh_data, only: xsize, ncells, dx
    use imc_global_part_data, only: n_input
    use imc_global_mat_data,  only: gamma, bee, tpower, tmp0
    use imc_global_phys_data, only: x15pi4, a, c

    implicit none

    character(len=*), intent(in)  :: input_file

    integer :: ifile_lun, io_status, pos1, pos2, n
    logical :: file_exists, eof
    character(len=64) :: file_line, test_token, keyw, keyv
    character(len=64), dimension(2) :: token

    real(kind=8) :: f_reqd, sf

    ifile_lun = imc_get_free_lun()

    inquire(file=trim(input_file), exist=file_exists)

    if (.not. file_exists) then
        write(*,*) 'Error: file does not exist: ', trim(input_file)
        stop
    endif

    open(unit=ifile_lun, file=trim(input_file), action='read', form='formatted', status='old')

    eof = .false.

    do while (.not. eof)

        ! Read the line, checking for errors and end-of-file
        read(ifile_lun,'(A)',iostat = io_status) file_line
        if (io_status < 0) exit ! EOF
        if (io_status > 0) then
          write(*,*) "Error reading line"
          write(*,*) trim(file_line)
          stop
        endif

        ! Tokenise the line into a two-element character array: keyword and key value
        pos1 = 1
        n = 0
        token(:) = ''  ! Reset for each line, in case any lines have fewer than 2 tokens
        do
            ! Scan for spaces and tabs
            pos2 = scan(file_line(pos1:), " "//achar(9))
            ! If scan returns 0, there are no spaces or tabs; put the entire remaining string in the next element
            if (pos2 == 0) then
                ! Check that the remaining string isn't just all whitespace first
                test_token = file_line(pos1:)
                if (len(trim(test_token)) > 0) then
                  n = n + 1
                  if (n > 2) then
                      write(*,*) 'Error: More than two tokens on input line'
                      stop
                  endif
                  token(n) = test_token
                endif
                exit
            endif
            ! If scan returns non-zero, extract the token
            test_token = file_line(pos1:pos1+pos2-2)
            pos1 = pos2+pos1
            ! Check the extracted subs-string isn't just whitesapce
            if (len(trim(test_token)) == 0) cycle
            n = n + 1
            if (n > 2) then
                write(*,*) 'Error: More than two tokens on input line'
                stop
            endif
            token(n) = test_token
        enddo

        ! Compare the tokens against the list of permitted input

        keyw = token(1)
        keyv = token(2)

        call to_lower(keyw)
        call to_lower(keyv)

        998 format(f64.32)
        999 format(i64)

        if (keyw == "dt") then
            read(keyv,998) dt

        elseif (keyw == 'xsize') then
            read(keyv,998) xsize

        elseif (keyw == "dx") then
            ! Round up the number of cells if not an integer, then if
            ! necessary adjust dx for the rounded up number of cells
            read(keyv,998) dx
            ncells = int(ceiling(xsize / dx))
            dx = xsize / float(ncells)

        elseif (keyw == "cycles") then
            read(keyv,999) ns

        elseif (keyw == "ns") then
            read(keyv,999) n_input

        elseif (keyw == "gamma") then
            read(keyv,998) gamma

        elseif (keyw == "scatterfrac") then
            read(keyv,998) sf
            f_reqd = 1. - sf
            bee = (4. * x15pi4 * a * c * &
                      f_reqd * gamma * dt / (1. - f_reqd))

        elseif (keyw == "t_power") then
            read(keyv,998) tpower

        elseif (keyw == "t_init") then
            read(keyv,998) tmp0

        else
            cycle

        endif

    enddo

    close(ifile_lun)

end subroutine imc_user_input_read


subroutine imc_user_input_echo()

    use imc_global_time_data, only: dt, ns
    use imc_global_mesh_data, only: xsize, ncells
    use imc_global_part_data, only: n_input, n_max
    use imc_global_mat_data,  only: gamma, bee, tpower, tmp0

    implicit none

    write(*,'(/,A79)') "========================================================================================="
    write(*,'(A)')     "User input"
    write(*,'(A79)')   "========================================================================================="

    write(*,*)
    write(*,'(A12,1X,I5)')      'mesh.ncells ', ncells
    write(*,'(A12,1X,F5.1)')    'mesh.xsize  ', xsize

    write(*,'(A12,1X,F5.1)')    'mat.gamma   ', gamma
    write(*,'(A12,1X,ES24.16)') 'mat.bee     ', bee
    write(*,'(A12,1X,F5.1)')    'mat.tpower  ', tpower
    write(*,'(A12,1X,F5.1)')    'mat.tmp0    ', tmp0

    write(*,'(A12,1X,F5.1)')    'time.dt     ', dt
    write(*,'(A12,1X,I5)')      'time.ns     ', ns

    write(*,'(A12,1X,I5)')      'part.n_input', n_input
    write(*,'(A12,1X,I5)')      'part.n_max  ', n_max

end subroutine imc_user_input_echo
