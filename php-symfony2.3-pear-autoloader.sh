#!/bin/sh

# NOTE: PEAR channel deprecated after 2.3.13
VERSION=2.3.13

RPM_SOURCEDIR=$(rpm --eval "%{_sourcedir}")
ARCHIVE=${RPM_SOURCEDIR}/php-symfony2.3-pear-autoloader-${VERSION}.tgz

if [ -e $ARCHIVE ]
then
    echo "## ARCHIVE: $ARCHIVE"
    exit 0
fi

TMP=$(mktemp --dir)
pushd $TMP

    echo -e "\n## CHANNEL"
    sudo pear channel-discover pear.symfony.com

    echo -e "\n## PACKAGES"
    pear list-all -c symfony2 | while read name version descr
    do
        if [ "$name" = "ALL" -o "$name" = "PACKAGE" -o "$version" = "" ]
        then
            continue
        fi
        pear download $name-$VERSION
        tar xf $(basename $name)-$VERSION.tgz --strip-components=1
    done

    AUTOLOAD_FILES=$(find Symfony -name autoloader.php)

popd

echo -e "\n## ARCHIVE: $ARCHIVE"
tar -cvzf $ARCHIVE -C $TMP $AUTOLOAD_FILES

echo -e "\n## CLEANUP"
rm -rf $TMP
