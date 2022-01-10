
platform = lin

items = ${platform} actioncode actionparse actionpool action actionutil bits character file storage swf tool util

all: ${items}
	#ounused ${logs}
	#ld ${obs}

logs :=
obs :=

%: %.s
	#o $<
	$(eval logs += $@.s.log)
	$(eval obs += $@.o)

install:

clean:
	-printf ' %s.s.log' ${items} | xargs rm -f
	-printf ' %s.o' ${items} | xargs rm -f

distclean:

uninstall:

test:

.PHONY: all install clean distclean uninstall test
