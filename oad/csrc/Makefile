OCOMP=o
OCONV=otoc
OLINK=ounused

compilerflags=-g -fsanitize=address
include ../cflags

src=../
platform=lin

include ../items

OFLAGS=x_file 2

obs=
logs=

$(foreach var,$(items),$(eval obs += ${var}.o))
$(foreach var,$(items),$(eval logs += ${src}${var}.oc.log))

all: libexte.a liboadbgdata.so

libexte.a: ${obs}
	$(AR) cr $@ $^

liboadbgdata.so: libexte.a main.o
	${OLINK} ${src}main.oc.log ${logs}
	$(CC) -shared main.o -o $@ -L. -l:libexte.a -Wl,--exclude-libs=libexte.a

%.o: ${src}%.oc
	${OCOMP} $< ${OFLAGS} include_sec 1
	${OCONV} $<.x import
	$(CC) -c -w -fPIC ${compilerflags} ${EXTRA_CFLAGS} ${src}$*.c -o $@

clean:
	-rm -f *.o libexte.a liboadbgdata.so

.PHONY: all clean
