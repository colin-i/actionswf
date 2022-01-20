
platform = lin

OFLAGS = conv_64 1
ifeq (${platform},win)
	OFLAGS += inplace_reloc 0
endif

syms=-s

name=example

all: ${name} uns lib lnk exe

uns:
	ounused ${name}.s.log

lib:
	if [ "${platform}" = "win" ]; then \
		i686-w64-mingw32-dlltool --no-leading-underscore -d ../lib/actionswf.def -l ./libactionswf.a; \
	fi

lnk:
	if [ "${platform}" = "lin" ]; then \
		$(LD) ${syms} -melf_i386 --dynamic-linker=/lib/ld-linux.so.2 ${name}.o -entry example_main -o ${name} -lc -L../src -l:actionswf.so; \
	else \
		i686-w64-mingw32-ld ${syms} ${name}.o -entry example_main -o ${name}.exe -L. -l:libactionswf.a; \
	fi
#$(LD) ${syms} --dynamic-linker=/lib64/ld-linux-x86-64.so.2 ${name}.o -entry example_main -o ${name} -lc -L../src -l:actionswf.so

exe:
	export LD_LIBRARY_PATH=../src; ./example

%: %.s
	o $< ${OFLAGS}

clean:
	-rm -f ${name}.s.log
	-rm -f ${name}.o
	-rm -f ${name}
	-rm -f ${name}.exe
	-rm -f libactionswf.a

.PHONY: all clean
# install distclean uninstall test
