CMP = doxygen

.PHONY: html github clean clobber

# Needs to be consistent with input to Doxygen in Doxyfile
markdown := $(wildcard *.md)
python := $(wildcard ../python/*/*.py)
fortran := $(wildcard ../fortran/*/*.f90)

# Find README.md
vpath %.md ..

doxygen.log: Doxyfile README.md $(markdown) $(python) $(fortran)
	$(CMP) > doxygen.log

html: doxygen.log

github:
	ghp-import --no-jekyll --no-history --push html

clean:
	rm -f doxygen.log

clobber: clean
	rm -rf html latex
