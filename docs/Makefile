FORD = ford
MKDOCS = mkdocs
MKDOCS_CFG = ../mkdocs.yml
MKDOCS_DOC_DIR = ../mkdocs/doc
MKDOCS_IMG_DIR = ../mkdocs/images/figures
SITE_DIR = ../site
FORD_DIR = ../doc
IMAGES_DIR = ../images/figures

.PHONY: html mkdocs sync-ford sync-images github clean clobber

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

sync-images:
	rm -rf $(MKDOCS_IMG_DIR)
	mkdir -p $(MKDOCS_IMG_DIR)
	cp -R $(IMAGES_DIR)/* $(MKDOCS_IMG_DIR)/

mkdocs: sync-ford sync-images
	$(MKDOCS) build -f $(MKDOCS_CFG)

html: ford.log mkdocs

clean:
	rm -f ford.log

clobber: clean
	rm -rf doc
	rm -rf $(MKDOCS_DOC_DIR)
	rm -rf $(MKDOCS_IMG_DIR)
