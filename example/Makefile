
syms=-s

name=example

all: ${name} uns lnk
	#./example

uns:
	ounused ${name}.s.log

lnk:
	$(LD) ${syms} -melf_i386 --dynamic-linker=/lib/ld-linux.so.2 ${name}.o -entry example_main -o ${name} -lc -L../src -l:actionswf.so

%: %.s
	o $< conv_64 1

install:

clean:
	-rm -f ${name}.s.log
	-rm -f ${name}.o
	-rm -f ${name}

distclean:

uninstall:

test:

.PHONY: all install clean distclean uninstall test
