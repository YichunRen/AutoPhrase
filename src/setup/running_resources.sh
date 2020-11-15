#!/bin/bash

cd /autophrase

# Creating symbolic link
ln -s data/tmp tmp

# Copying src
mkdir src
cp -r resources/AutoPhrase/src/* src/

# Getting tools setted up
mkdir tools
echo ' => Copying tools from AutoPhrase...'
cp -r resources/AutoPhrase/tools/* tools

# Copying makefile
cp recourses/Makefile .
