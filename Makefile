
MEDTARGETS := test clean distclean
TOPTARGETS := all install uninstall
#distclean is called at launchpad build, for here if there were configures

SUBDIRS := dev src oad
ALLDIRS := example $(SUBDIRS)

ifndef prefix
prefix=/usr
endif

ifeq ($(shell dpkg-architecture -qDEB_HOST_ARCH), i386)
conv_64=1
else
conv_64=0
endif

$(TOPTARGETS): $(SUBDIRS)
$(MEDTARGETS): $(ALLDIRS)
$(ALLDIRS):
	$(MAKE) -C $@ conv_64=${conv_64} $(MAKECMDGOALS)

test:
	RUN__SHELL=$(SHELL) . ./shl && cd tests && conv_64=${conv_64} RUN__SHELL="$${RUN__SHELL}" $${RUN__SHELL} ./as && conv_64=${conv_64} $${RUN__SHELL} ./c 1 && \
	cd ffdec && conv_64=${conv_64} RUN__SHELL="$${RUN__SHELL}" $${RUN__SHELL} ./as && \
	cd ../data && conv_64=${conv_64} RUN__SHELL="$${RUN__SHELL}" $${RUN__SHELL} ./test x && echo tests ok
clean:
	RUN__SHELL=$(SHELL) . ./shl && cd tests && $${RUN__SHELL} ./c && cd ffdec && $${RUN__SHELL} ./c && cd ../data && $${RUN__SHELL} ./c
install:
	install -D oaalternative $(DESTDIR)$(prefix)/bin/oaalternative
uninstall:
	-rm -f $(DESTDIR)$(prefix)/bin/oaalternative

.PHONY: $(TOPTARGETS) $(MEDTARGETS) $(ALLDIRS)
.NOTPARALLEL:
