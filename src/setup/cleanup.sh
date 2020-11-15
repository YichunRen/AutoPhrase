#!/bin/bash

if [ -d "bin" ]; then
    rm -rf bin/
fi

if [ -d "tmp" ]; then
    rm -rf tmp/
fi

if [ -d "tools" ]; then
    rm -rf tmp/
fi

rm Makefile
rm tmp

cp -r data/models/ data/output/
