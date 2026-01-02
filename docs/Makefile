FORD = ford
MKDOCS = mkdocs
MKDOCS_CFG = ../mkdocs.yml
MKDOCS_DOC_DIR = ../mkdocs/doc
SITE_DIR = ../site
FORD_DIR = ../doc

.PHONY: html mkdocs sync-ford github clean clobber

# Needs to be consistent with input to Doxygen in Doxyfile
markdown := $(wildcard *.md)
python := $(wildcard ../python/*/*.py)
fortran := $(wildcard ../fortran/*/*.f90)

# Find README.md
vpath %.md ..

ford.log: README.md $(markdown) $(python) $(fortran)
	$(FORD) ../ford.md > ford.log 2>&1

sync-ford: ford.log
	rm -rf $(MKDOCS_DOC_DIR)
	mkdir -p $(MKDOCS_DOC_DIR)
	cp -R $(FORD_DIR)/* $(MKDOCS_DOC_DIR)/

mkdocs: sync-ford
	$(MKDOCS) build -f $(MKDOCS_CFG)

html: ford.log mkdocs

clean:
	rm -f ford.log

clobber: clean
	rm -rf doc
	rm -rf $(MKDOCS_DOC_DIR)
