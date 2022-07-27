NAME = imc

CMP = gfortran

#FFLAGS = -fbounds-check -g -pedantic -Wall -O #-pg
FFLAGS = -Ofast
#FFLAGS = -fopenmp
#LFLAGS =

OBJECTS = \
          imc_global_bcon_data.o \
          imc_global_mat_data.o  \
          imc_global_mesh_data.o \
          imc_global_part_data.o \
          imc_global_phys_data.o \
          imc_global_time_data.o \
          imc_utils.o            \
          imc_user_input.o       \
          imc_mesh.o             \
          imc_update.o           \
          imc_source.o           \
          imc_track.o            \
          imc_tally.o            \
          imc_opcon.o            \
          imc.o

MODULES = \
          imc_global_bcon_data.mod \
          imc_global_mat_data.mod  \
          imc_global_mesh_data.mod \
          imc_global_part_data.mod \
          imc_global_phys_data.mod \
          imc_global_time_data.mod \
          imc_utils.mod

#NUM_PROCS ?= 2

.PHONY: clean clobber test

test: $(NAME).exe
	./imc.exe -h
	./imc.exe

$(NAME).exe: $(MODULES) $(OBJECTS)
	$(CMP) $(FFLAGS) $(LFLAGS) $(OBJECTS) -o $(NAME).exe

%.o :  %.f90
	$(CMP) $(FFLAGS) -c $<

%.mod: %.f90
	$(CMP) $(FFLAGS) -c $<

clean:
	rm -f *.o *.mod

clobber: clean
	rm -f *.exe
