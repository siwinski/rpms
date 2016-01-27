# vim: tabstop=4:softtabstop=4:shiftwidth=4:noexpandtab

SPEC_DIR := $(shell pwd)
SPEC := $(shell ls $(SPEC_DIR)/*.spec | head -1)
SPEC_NAME := $(shell basename $(SPEC) | sed 's/\.spec//')

SOURCES_DIR := $(shell rpm --eval="%{_sourcedir}")



.PHONY: setup
setup:
	@which rpmbuild >& /dev/null || sudo yum install -y rpm-build
	@(which rpmdev-setuptree && which spectool) >& /dev/null || sudo yum install -y rpmdevtools
	@rpmdev-setuptree



.PHONY: sources
sources:
	spectool -g -R $(SPEC)
	cp \
		drupal8-find-provides.php \
		drupal8-find-requires.php \
		drupal8-modify-core-composer-json.php \
		drupal8-prep-licenses-and-docs.sh \
		$(SOURCES_DIR)



.PHONY: rpms
rpms:
	rpmbuild -ba $(SPEC)



.PHONY: debug
debug:
	@echo " SOURCES_DIR: $(SOURCES_DIR)"
	@echo "  COMMON_DIR: $(COMMON_DIR)"
	@echo "    SPEC_DIR: $(SPEC_DIR)"
	@echo "        SPEC: $(SPEC)"
	@echo "   SPEC_NAME: $(SPEC_NAME)"
