CMP = doxygen

.PHONY: github clean clobber

html: Doxyfile *.md ../python/src/*.py ../fortran/src/*.f90
	$(CMP) > doxygen.log

github:
	ghp-import --no-jekyll --no-history --push html

clean:
	rm -f doxygen.log

clobber: clean
	rm -rf html latex
