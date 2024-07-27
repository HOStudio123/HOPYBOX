# Makefile for Sphinx documentation

# The source directory
SOURCEDIR = .
# The build directory
BUILDDIR = _build

# The command to use to build the documentation
SPHINXBUILD = sphinx-build
# Options to pass to sphinx-build
SPHINXOPTS = -d $(BUILDDIR)/doctrees

.PHONY: all clean html

all: html

html:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html $(SPHINXOPTS)

clean:
	rm -rf $(BUILDDIR)/html $(BUILDDIR)/doctrees
