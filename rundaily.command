#!/bin/sh
#note: this file itself must be a executable file!!!

#this does not work when the directory contains "blank"
#basepath=$(cd `dirname $0`; pwd)
#echo "$basepath"

basepath="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
#echo "$basepath"

cd /users/feiqizhang &&
/users/feiqizhang/anaconda/bin/python3.6 "$basepath""/crawler.py"


