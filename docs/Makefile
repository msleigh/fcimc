.PHONY: ford html mkdocs sync-ford sync-images clean clobber

# Needs to be consistent with input to Ford
markdown := $(wildcard *.md)
python := $(wildcard ../python/*/*.py)
fortran := $(wildcard ../fortran/*/*.f90)

FORD := ford
MKDOCS := mkdocs

MKDOCS_DIR := ../mkdocs
MKDOCS_CFG := $(MKDOCS_DIR)/mkdocs.yml

MKDOCS_DOC_DIR := $(MKDOCS_DIR)/doc
MKDOCS_IMG_DIR := $(MKDOCS_DIR)/images/figures
MKDOCS_SITE_DIR := ../site
FORD_DIR := ../doc
FORD_OUT_DIR := doc
FORD_OUT := $(FORD_DIR)/index.html
REFERENCE_IMAGES := ../images/figures

# Find README.md
vpath %.md ..

html: mkdocs

mkdocs: sync-ford sync-images
	$(MKDOCS) build -f $(MKDOCS_CFG)

sync-ford: $(FORD_OUT)
	rm -rf $(MKDOCS_DOC_DIR)
	mkdir -p $(MKDOCS_DOC_DIR)
	cp -R $(FORD_DIR)/* $(MKDOCS_DOC_DIR)/

$(FORD_OUT): README.md $(markdown) $(python) $(fortran) ../ford.md ../fpm.toml
	$(FORD) -o $(FORD_OUT_DIR) ../ford.md > ford.log 2>&1

ford: $(FORD_OUT)

sync-images:
	rm -rf $(MKDOCS_IMG_DIR)
	mkdir -p $(MKDOCS_IMG_DIR)
	cp -R $(REFERENCE_IMAGES)/* $(MKDOCS_IMG_DIR)/

clean:
	rm -f ford.log
	rm -rf $(MKDOCS_DOC_DIR)
	rm -rf $(MKDOCS_IMG_DIR)

clobber: clean
	rm -rf $(FORD_DIR)
	rm -rf $(MKDOCS_SITE_DIR)
