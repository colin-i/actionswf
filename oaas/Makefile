
#this lib is helping oaas3 to shortcut the repeatable translation calls

ifndef OCOMP
OCOMP=o
endif
ifndef OLINK
OLINK=ounused
endif
ifndef OCONV
OCONV=otoc
endif
ifndef linkerflags
linkerflags=-O3 -s
endif
ifndef compilerflags
compilerflags=${linkerflags}
endif
ifndef EXTRA_CFLAGS
include ../oad/cflags
endif
ifndef prefix
prefix=/usr
endif

ifeq (${conv_64},1) #to cross compile
	ifneq ($(CC),arm-linux-gnueabihf-gcc)
		model=-m32
	endif
endif

OFLAGS=x_file 2

libname=liboaas.so

objs=util.o
objects=main.o
exte=libexte.a

all: ${headers} ${libname}

headers:
	$(MAKE) -C ../include

${libname}: ${objects} ${exte}
	${OLINK} main.oc.log util.oc.log
	$(CC) ${model} ${linkerflags} -shared $< -o ${libname} -L. -l:${exte} -Wl,--exclude-libs=${exte}

${exte}: ${objs}
	$(AR) cr ${exte} $^

%.o: %.oc
	${OCOMP} $< ${OFLAGS} include_sec 1
	${OCONV} ${OCONVFLAGS} $<.x import
	$(CC) ${model} -c -w -fPIC ${compilerflags} ${EXTRA_CFLAGS} $*.c

clean:
	-rm -f main.oc.log main.oc.x main.c util.oc.log util.oc.x util.c
	-rm -f ${objects} ${exte} ${objs} ${libname}

distclean: clean

test:
	echo "Nothing"

install-lib:
	install -D ${libname} $(DESTDIR)$(prefix)/lib/${libname}

install: all install-lib

uninstall:
	-rm -f $(DESTDIR)$(prefix)/lib/${libname}

.PHONY: all headers install install-lib clean distclean uninstall test
