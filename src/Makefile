
platform = lin

items = ${platform} actioncode actionparse actionpool action actionutil bits character file storage swf tool util ../shared/action_dllmain

all: ${items}
	ounused ${logs}
	#ld ${obs}

logs :=
obs :=

%: %.s
	o $< conv_64 1
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
