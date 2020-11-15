#!/bin/bash

cd /autophrase

# Setting up run time directories
mkdir models
mkdir data
cd data
mkdir tmp
mkdir models
mkdir raw
mkdir output
mkdir report
cd ..

# Set directory permissions
chmod 755 run_phrasing.sh;
chmod 755 src/setup/*.sh
chmod 755 src/data/*.sh

# Creating symbolic link
ln -s data/tmp tmp

# Copying src
cp -r resources/AutoPhrase/src/* src/

# Getting tools setted up
mkdir tools
echo ' => Copying third party tools from AutoPhrase...'
cp -r resources/AutoPhrase/tools/* tools
cp resources/Makefile .
