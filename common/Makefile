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
	@if [ -z "$(NO_SPECTOOL)" ]; \
	then \
		spectool -g -R $(SPEC); \
	fi

	@if [ -n "$(GET_SOURCE_GITHUB)" ]; \
	then \
		$(COMMON_DIR)/get-source-github.sh $(SPEC); \
		cp $(COMMON_DIR)/get-source-github.sh $(SOURCES_DIR)/$(SPEC_NAME)-get-source.sh; \
	fi



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
