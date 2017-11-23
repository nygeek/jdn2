#
# Julian Day Number tools
# Starting from scratch 2017-11-12
# by Marc Donner (marc.donner@gmail.com)
#

DIRS = "."
DIRPATH="~/projects/j/jdn"
BINRELPATH="../projects/j/jdn"

HOSTS = waffle pancake
PUSH_FILES = $(HOSTS:%=.%_push)

help: ${FORCE}
	cat Makefile

SOURCE = \
	jdn.py \
	julian \
	julian.py \
	nailuj.py \
	testjdn.py

FILES = \
	${SOURCE} \
	.gitattributes \
	Makefile

stuff.tar: ${FORCE}
	tar -cvf stuff.tar ${FILES}

test: ${FORCE}
	python testjdn.py

install: ${FORCE}
	- rm -f ~/bin/julian
	- rm -f ~/bin/nailuj
	(cd ~/bin; ln -s ${BINRELPATH}/julian julian)
	(cd ~/bin; ln -s ${BINRELPATH}/nailuj nailuj)

# DATA = sample.txt

pylint: ${SOURCE}
	pylint ${SOURCE}

# GIT operations

diff: .gitattributes
	git diff

commit: .gitattributes
	git commit ${FILES}

log: .gitattributes
	git log --pretty=oneline

# Distribution to other hosts

push: ${PUSH_FILES}
	rm ${PUSH_FILES}

.%_push:
	rsync -az --exclude=".git*" --exclude=".*_push" -e ssh ${DIRS} $*:${DIRPATH}
	touch $@

FORCE: 
