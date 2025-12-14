CMP = ford

.PHONY: html github clean clobber

# Needs to be consistent with input to Doxygen in Doxyfile
markdown := $(wildcard *.md)
python := $(wildcard ../python/*/*.py)
fortran := $(wildcard ../fortran/*/*.f90)

# Find README.md
vpath %.md ..

ford.log: README.md $(markdown) $(python) $(fortran)
	$(CMP) ../ford.md > ford.log 2>&1

html: ford.log

clean:
	rm -f ford.log

clobber: clean
	rm -rf doc
