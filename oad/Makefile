
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

OFLAGS=x_file 2

libname=liboadbgdata.so

all: ${libname} oadbgdatai.h
re:
	$(MAKE) clean
	$(MAKE) all

%.oh: %.h.oh
	echo "format elfobj64" > $@
	echo "orphan off" >> $@
	cat $< >> $@
%.h: %.oh
	${OCOMP} $< ${OFLAGS}
	${OCONV} $<.x

${libname}: main.o
	${OLINK} main.oc.log
	@echo
	$(CC) ${linkerflags} -shared $< -o ${libname}
	# `pkg-config --libs gtk4`

%.o: %.oc
	${OCOMP} $< ${OFLAGS}
	${OCONV} $<.x
	$(CC) -c -w ${compilerflags} $*.c

clean:
	-rm -f main.o
	-rm -f main.oc.log
	-rm -f main.oc.x
	-rm -f main.c
	-rm -f ${libname}
	-rm -f oadbgdatai.oh.log
	-rm -f oadbgdatai.oh.x
	-rm -f oadbgdatai.oh
	-rm -f oadbgdatai.h

distclean: clean

test:
	echo "Nothing"

install-lib:
	install -D ${libname} \
		$(DESTDIR)$(prefix)/lib/${libname}

install: all install-lib

uninstall:
	-rm -f $(DESTDIR)$(prefix)/lib/${libname}

#.PHONY: all install clean distclean uninstall test
