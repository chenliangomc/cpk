#
#=2015-1110-1843.28est on lcpc
#

all:	run

doc:
	pydoc -w conf
	pydoc -w pathconf

run:
	./demoapp.py

test:
	@echo "not implemented yet."

#-eof-#