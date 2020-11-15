#!/bin/bash
cd /autophrase

if [ -d "bin" ]; then
    rm -rf bin/
fi

if [ -d "tmp" ]; then
    rm -rf tmp/
fi

if [ -d "tools" ]; then
    rm -rf tools/
fi

rm Makefile
rm tmp
rm run_phrasing.sh

cp -r data/models/ data/out/
