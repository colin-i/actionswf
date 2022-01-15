
platform = lin

items = ${platform} actioncode actionparse actionpool actionutil bits character file storage util
expitems = action swf tool ../shared/action_dllmain

exte=libexte.a

syms =-s

name = actionswf.so

all: ${items} ${expitems}
	ounused ${logs}
	$(AR) cr ${exte} ${obs}
	$(LD) ${syms} -melf_i386 --dynamic-linker=/lib/ld-linux.so.2 ${eobs} -shared -entry DllMain -o ${name} -lc -L. -l:libexte.a --exclude-libs ${exte}

logs :=
obs :=
eobs :=

%: %.s
	o $< conv_64 1
	$(eval logs += $@.s.log)
	$(eval obs += $@.o)
%: %.es
	o $< conv_64 1
	$(eval logs += $@.es.log)
	$(eval eobs += $@.o)

clean:
	-printf ' %s.s.log' ${items} | xargs rm -f
	-printf ' %s.es.log' ${expitems} | xargs rm -f
	-printf ' %s.o' ${items} ${expitems} | xargs rm -f
	-rm -f ${exte}
	-rm -f ${name}

distclean:

install:

uninstall:

test:

.PHONY: all install clean distclean uninstall test
