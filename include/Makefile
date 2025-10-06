
ifndef platform
platform=lin
endif
ifndef OCOMP
OCOMP=o
endif
ifndef OCONV
OCONV=otoc
endif

items=action ascii ${platform}home ${platform} prog program xlog
$(foreach var,$(items),$(eval headers += ${var}.h))
$(foreach var,$(items),$(eval xfiles += ${var}.ohi.x))

include ../src/items
include ../src/hitems
$(foreach var,$(hreqs),$(eval chreqs += ../include/${var}.h))

all: ${ohreqs} ${chreqs} ${headers}

include ../src/rules

%.h: %.ohi
	${OCOMP} $< x_file 2 logfile 0 include_sec 1
	${OCONV} $<.x
%.ohi: %.oh
	echo "format elfobj64" > $@
	echo "orphan off" >> $@
	cat $< >> $@
lin.ohi: lin.oh
	echo "format elfobj64" > $@
	echo "orphan off" >> $@
	cat $< >> $@
	sed -i "s/^const path_separator=Slash/const path_separator=`cat ascii.oh | grep -Po '(?<=Const Slash=).*'`/" $@
${chreqs}:
	ln -s `echo $* | sed s/platform/${platform}/`.h $@

clean:
	-rm -f ${xfiles} lin.ohi ${headers} ${ohreqs} ${chreqs}
distclean: clean

.PHONY: all clean distclean
