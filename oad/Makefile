
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
include ./cflags
endif
ifndef prefix
prefix=/usr
endif
ifndef platform
platform=lin
endif

ifeq (${conv_64},1) #to cross compile
	ifneq ($(CC),arm-linux-gnueabihf-gcc)
		model=-m32
	endif
else
#	model=
	ifeq (${platform},win) #to long long
		OCONVFLAGS=-
	endif
endif

OFLAGS=x_file 2

libfirstname=liboadbgdata
libname=${libfirstname}.so
libnamedll=${libfirstname}.dll
exte=libexte.a

all: ${libname} oadbgdata.h
oadbgdata.h: oadbgdatas.h #anyway will do it at objects

re:
	$(MAKE) clean
	$(MAKE) all

xlog=../include/xlog.

items=intern compare frame string branch ibranch log save mark ${platform}
#$(eval subobjects = )
$(foreach var,$(items),$(eval subobjects += ${var}.o))
#$(eval sublogs = )
$(foreach var,$(items),$(eval sublogs += ${var}.oc.log))
#$(eval subx = )
$(foreach var,$(items),$(eval subx += ${var}.oc.x))
#$(eval subc = )
$(foreach var,$(items),$(eval subc += ${var}.c))

objects=main.o ${subobjects}
${objects}: common.h
common.h: oadbgdatas.h ${xlog}h
${exte}: ${subobjects}
	$(AR) cr ${exte} $^
${libname}: main.o ${exte}
	${OLINK} main.oc.log ${sublogs}
	if [ "${platform}" = "lin" ]; then \
		$(CC) ${model} ${linkerflags} -shared $< -o ${libname} -L. -l:${exte} -Wl,--exclude-libs=${exte}; \
	else \
		x86_64-w64-mingw32-gcc --no-leading-underscore ${linkerflags} ${objects} -shared -lmsvcrt -o ${libnamedll} -Wl,--exclude-modules-for-implib `printf ',%s' ${subobjects} | cut -c2-`; \
	fi
# -l:intern.o ? is ok but exclude-libs intern.o/libintern.a will not exclude

%.o: %.oc
	${OCOMP} $< ${OFLAGS}
	${OCONV} ${OCONVFLAGS} $<.x import
	$(CC) ${model} -c -w -fPIC ${compilerflags} ${EXTRA_CFLAGS} $*.c
#-Wno are a must at pkgbuild
#-fPIC since launchpad bionic build
#-Wimplicit-function-declaration is good but anyway when making .x, ocompiler is also checking for this error
%.ohi: %.oh
	echo "format elfobj64" > $@
	echo "orphan off" >> $@
	echo "override include_sec 1" >> $@
	cat $< >> $@
%.h: %.ohi
#	if [ $@ = common.h ]; then $(MAKE) ${xlog}h;fi
	${OCOMP} $< ${OFLAGS} logfile 0
	${OCONV} ${OCONVFLAGS} $<.x

clean:
	-rm -f common.ohi            common.ohi.x     common.h
	-rm -f ${xlog}ohi            ${xlog}ohi.x     ${xlog}h
	-rm -f oadbgdatas.ohi        oadbgdatas.ohi.x oadbgdatas.h
	-rm -f ${objects} ${sublogs} ${subx}          ${subc}
	-rm -f           main.oc.log main.oc.x        main.c
	-rm -f oadbgdata.ohi         oadbgdata.ohi.x  oadbgdata.h

	-rm -f ${exte} ${libname} ${libnamedll}

distclean: clean

test:
	echo "Nothing"

install-lib:
	install -D ${libname} $(DESTDIR)$(prefix)/lib${install_number}/${libname}
	if [ -e ../include_dev ]; then \
		install -D oadbgdata.h $(DESTDIR)$(prefix)/include/actionswf/oadbgdata.h && \
		install -D oadbgdatas.h $(DESTDIR)$(prefix)/include/actionswf/oadbgdatas.h && \
		install -D oadbgdata.oh $(DESTDIR)$(prefix)/include/actionswf/oadbgdata.oh && \
		install -D oadbgdatas.oh $(DESTDIR)$(prefix)/include/actionswf/oadbgdatas.oh; \
	fi

install: all install-lib

uninstall:
	-rm -f $(DESTDIR)$(prefix)/lib${install_number}/${libname}
	-if [ -e ../include_dev ]; then \
		rm -f $(DESTDIR)$(prefix)/include/actionswf/oadbgdata.h; \
		rm -f $(DESTDIR)$(prefix)/include/actionswf/oadbgdatas.h; \
		rm -f $(DESTDIR)$(prefix)/include/actionswf/oadbgdata.oh; \
		rm -f $(DESTDIR)$(prefix)/include/actionswf/oadbgdatas.oh; \
	fi

#.PHONY targets are not default files, then, make will not try to test if a rule has an updated file on the disk (if has will skip that rule)
.PHONY: all install install-lib clean distclean uninstall test re
#tested: .NOTPARALLEL: in parent is not preserved here
