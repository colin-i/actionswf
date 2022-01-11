
platform = lin

items = ${platform} actioncode actionparse actionpool action actionutil bits character file storage swf tool util ../shared/action_dllmain

syms =-s

name = actionswf.so

all: ${items}
	ounused ${logs}
	#--exclude-modules-for-implib and --exclude-symbols are for PE only not elf
	#`printf ',%s.s.log' ${items} | cut -c2-`
	$(LD) ${syms} -melf_i386 --dynamic-linker=/lib/ld-linux.so.2 ${obs} -shared -entry DllMain -o ${name} -lc

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
	-rm -f ${name}

distclean:

uninstall:

test:

.PHONY: all install clean distclean uninstall test
