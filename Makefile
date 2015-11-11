#
#=2015-1110-1843.28est on lcpc
#

all:	run

doc:
#	pydoc -w conf
#	pydoc -w pathconf
	epydoc -v --url "https://github.com/chenliangomc/cpk" --name "common Python toolkit"  conf pathconf runtool

run:
	./demoapp.py

test:
	@echo "not implemented yet."

#-eof-#