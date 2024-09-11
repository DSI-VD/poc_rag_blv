#!/bin/bash
# Get Actes data You need the key
#
# Usage: ./get_actes.sh key

KEY=$1
if [ -z "$KEY" ]; then
    echo "Please provide a key. Usage: ./get_actes.sh key"
    exit 1
fi

DIR="./Actes"
if [ ! -d "$DIR" ]; then
    mkdir $DIR
    echo -e "# Ignore everything in this directory Except this file\n*" > $DIR/.gitignore
fi



URL="https://r2.ilab-dgnsi-vd.ch/${KEY}.zip"

pushd $DIR
wget --tries 2 --show-progress --quiet --output-document=${KEY}.zip $URL
if [ $? -ne 0 ]; then
    echo "wget error."
    exit 2
fi
unzip -oq ${KEY}.zip
if [ $? -ne 0 ]; then
    echo "unzip error."
    rm ${KEY}.zip
    exit 4
fi
rm ${KEY}.zip
popd

exit 0
