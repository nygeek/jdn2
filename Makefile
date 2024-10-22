#
# Julian Day Number tools
# Starting from scratch 2017-11-12
# by Marc Donner (marc.donner@gmail.com)
#
# $Id$
#

PYTHON := /usr/local/bin/python2
PYLINT := ${PYTHON} -m pylint

DIRS = "."
DIRPATH="~/projects/j/jdn2"
BINRELPATH="../projects/j/jdn2"

.PHONY: help
help:
	cat Makefile

SOURCE = \
	jdn.py \
	julian.py \
	nailuj.py \
	test2.py

FILES = \
	${SOURCE} \
	.gitattributes \
	julian.sh \
	nailuj.sh \
	Makefile \
	pylintrc \
	README.md \
	test.out \
	test.reference

.PHONY: stuff.tar
stuff.tar:
	tar -cvf stuff.tar ${FILES}

.PHONY: test
test:
	${PYTHON} test2.py > test.out
	diff test.out test.reference

.PHONY: install
install:
	- rm -f ~/bin/julian
	- rm -f ~/bin/nailuj
	(cd ~/bin; ln -s ${BINRELPATH}/julian.sh julian)
	(cd ~/bin; ln -s ${BINRELPATH}/nailuj.sh nailuj)

lint: ${SOURCE}
	${PYLINT} ${SOURCE}

# GIT operations

diff: .gitattributes
	git diff

commit: .gitattributes
	git commit ${FILES}

log: .gitattributes
	git log --pretty=oneline
