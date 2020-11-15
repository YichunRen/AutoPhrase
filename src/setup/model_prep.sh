#!/bin/bash

# Start compiling
cp /autophrase/src/setup/compile.sh /autophrase
bash compile.sh

# Cleanning up
rm /autophrase/compile.sh
