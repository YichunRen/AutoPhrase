#!/bin/bash

if [ -d "bin" ]; then
    rm -rf bin/
fi

if [ -d "tmp" ]; then
    rm -rf tmp/
fi

rm Makefile
