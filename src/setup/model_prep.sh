#!/bin/bash

# Start compiling
cp src/setup/compile.sh .
bash compile.sh

# Cleanning up
rm compile.sh
