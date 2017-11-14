#!/bin/sh
#note: this file itself must be a executable file!!!


basepath=$(cd `dirname $0`; pwd)

cd /users/feiqizhang &&

/users/feiqizhang/anaconda/bin/python3.6 $basepath"/crawler.py"


