#!/bin/bash
# A shell script to clean malicious code from a website
# Author: Samuel Searles-Bryant
# Date: 2018-11-03
# -------------------------------------------------------
# Set vars
site_dir=$1
patterns=$2

if ! [ $# -eq 2 ]; then
    echo "usage: $0 site_directory pattern_file"
    exit 1
fi

for filename in $(find $site_dir -type f);
do
    sed -E -f $patterns -i "" $filename
done
