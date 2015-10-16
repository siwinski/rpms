#!/bin/bash

CHANGELOG_DATE=`date +"%a %b %d %Y"`
SPEC_TEMPLATE="drupal7-TEMPLATE.spec"
README_TEMPLATE="drupal7-TEMPLATE-RPM-README.txt"

for DRUPAL_MACHINE_NAME in $@; do
	echo "-------------------- ${DRUPAL_MACHINE_NAME} --------------------"
	SPEC="drupal7-${DRUPAL_MACHINE_NAME}.spec"
	README="drupal7-${DRUPAL_MACHINE_NAME}-RPM-README.txt"

	cat ${SPEC_TEMPLATE} | sed -e "s/__MODULE__/${DRUPAL_MACHINE_NAME}/" -e "s/ddd MMM DD YYYY/${CHANGELOG_DATE}/" > ${SPEC}
	#cp ${README_TEMPLATE} ${README}
done
