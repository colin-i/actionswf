TOPTARGETS := all install clean distclean uninstall test

SUBDIRS := src

$(TOPTARGETS): $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)
.PHONY: $(TOPTARGETS) $(SUBDIRS)

all:
	cd ./src; ounused
