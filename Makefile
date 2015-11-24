#
#=2015-1110-1843.28est on lcpc
#

DOPT = -v --url "https://github.com/chenliangomc/cpk" --name "common Python toolkit"  --output "apidoc"

#all:	run

doc:
	epydoc $(DOPT)  conf pathconf runtool

run:
	./demoapp.py

test:
	@echo "not implemented yet."

#-eof-#