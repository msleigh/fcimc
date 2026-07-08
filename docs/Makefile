.PHONY: ford html mkdocs zensical sync-ford sync-images clean clobber

# Needs to be consistent with input to Ford
markdown := $(wildcard *.md)
python := $(wildcard ../python/*/*.py)
fortran := $(wildcard ../fortran/*/*.f90)

FORD := uv run --no-default-groups --group ford ford
MKDOCS := uv run mkdocs
ZENSICAL := uv run --no-default-groups --group zensical zensical

MKDOCS_DIR := ../mkdocs
MKDOCS_CFG := $(MKDOCS_DIR)/mkdocs.yml

MKDOCS_DOC_DIR := $(MKDOCS_DIR)/doc
MKDOCS_IMG_DIR := $(MKDOCS_DIR)/images/figures
MKDOCS_SITE_DIR := ../site
ZENSICAL_SITE_DIR := $(MKDOCS_DIR)/site
FORD_DIR := html
FORD_OUT := $(FORD_DIR)/index.html
REFERENCE_IMAGES := ../images/figures

html: mkdocs

mkdocs: sync-ford sync-images
	$(MKDOCS) build -f $(MKDOCS_CFG)

zensical: sync-ford sync-images
	FCIMC_SITE_DIR=site $(ZENSICAL) build -f $(MKDOCS_CFG)

sync-ford: $(FORD_OUT)
	rm -rf $(MKDOCS_DOC_DIR)
	mkdir -p $(MKDOCS_DOC_DIR)
	cp -R $(FORD_DIR)/* $(MKDOCS_DOC_DIR)/

$(FORD_OUT): ford.md $(markdown) $(python) $(fortran)
	$(FORD) ford.md

ford: $(FORD_OUT)

sync-images:
	rm -rf $(MKDOCS_IMG_DIR)
	mkdir -p $(MKDOCS_IMG_DIR)
	cp -R $(REFERENCE_IMAGES)/* $(MKDOCS_IMG_DIR)/

clean:
	rm -rf $(MKDOCS_DOC_DIR)
	rm -rf $(MKDOCS_IMG_DIR)

clobber: clean
	rm -rf $(FORD_DIR)
	rm -rf $(MKDOCS_SITE_DIR)
	rm -rf $(ZENSICAL_SITE_DIR)
