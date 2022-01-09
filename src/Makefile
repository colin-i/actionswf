
all: swf action
	echo ${CFLAGS}

CFLAGS := q

%: %.s
	echo 111 $@.o $<
	$(eval CFLAGS += w)

.PHONY: all install clean distclean uninstall test
