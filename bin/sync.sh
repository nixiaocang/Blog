#!/bin/bash

CURDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $CURDIR

. env.sh

/usr/bin/python $CURDIR/../script/check_sync.py