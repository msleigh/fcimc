CMP = doxygen

.PHONY: clean clobber

html: Doxyfile *.md ../python/src/*.py ../fortran/src/*.f90
	$(CMP) > doxygen.log

clean:
	rm -rf doxygen.log

clobber: clean
	rm -rf html latex
