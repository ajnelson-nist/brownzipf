#!/usr/bin/make -f

# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to title 17 Section 105 of the
# United States Code this software is not subject to copyright
# protection and is in the public domain. NIST assumes no
# responsibility whatsoever for its use by other parties, and makes
# no guarantees, expressed or implied, about its quality,
# reliability, or any other characteristic.
#
# We would appreciate acknowledgement if the software is used.

PYTHON2 ?= python2.7
PYTHON3 ?= python3.4

all: \
  demo \
  brownzipf2 \
  brownzipf3

.PHONY: \
  demo \
  download \
  brownzipf2 \
  brownzipf3

brown_downloaded.log: \
  confirm_brown_downloaded.py
	$(PYTHON3) confirm_brown_downloaded.py || (echo "ERROR:Makefile:Brown corpus not found.  Download the corpus with 'make -C $$PWD download'.  Note this is a GUI operation." >&2 ; exit 1)
	touch $@

brownzipf2: \
  brownzipf2.png
	open $<

#Generate the plot with Python 2.
brownzipf2.png: \
  brownzipf.py \
  brown_downloaded.log
	rm -f _$@
	$(PYTHON2) brownzipf.py _$@
	mv _$@ $@

brownzipf3: \
  brownzipf3.png
	open $<

#Generate the plot with Python 3.
brownzipf3.png: \
  brownzipf.py \
  brown_downloaded.log
	rm -f _$@
	$(PYTHON3) brownzipf.py _$@
	mv _$@ $@

demo: \
  demo.png
	open $<

demo.png: \
  brown_downloaded.log \
  demo.py
	$(PYTHON2) demo.py

download: \
  download_brown.py
	$(PYTHON3) download_brown.py
