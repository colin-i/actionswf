
ifndef OCOMP
OCOMP=o
endif
ifndef OCONV
OCONV=otoc
endif

all: flags.h flagss.h
%.h: %.ohi
	${OCOMP} $< x_file 2 logfile 0
	${OCONV} $<.x
%.ohi: %.oh
	echo "format elfobj64" > $@
	echo "orphan off" >> $@
	echo "override include_sec 1" >> $@
	cat $< >> $@

test:
	echo dev
clean:
	-rm -f flags.ohi.x flagss.ohi.x flags.ohi flagss.ohi flags.h flagss.h
distclean: clean

install:
	if [ -e ../include_dev ]; then \
		install -D flags.h $(DESTDIR)$(prefix)/include/actionswf/flags.h && \
		install -D flags.h $(DESTDIR)$(prefix)/include/actionswf/flagss.h; \
	fi
uninstall:
	-if [ -e ../include_dev ]; then \
		rm -f $(DESTDIR)$(prefix)/include/actionswf/flags.h; \
		rm -f $(DESTDIR)$(prefix)/include/actionswf/flagss.h; \
	fi

.PHONY: all install clean distclean uninstall test
