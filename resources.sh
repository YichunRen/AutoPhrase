#!/bin/bash

# Note: this is the script that collects needed resources from AutoPhrase repo from Prof. Shang
# It also creates needed symbolic link into the root directory
############ Configure Needed Files ############
# Dowload from autophrase
echo ' => Downloading needed files...'
if [ -d "resources" ]; then
    echo ' => resources dir exists!'
else
    mkdir resources
fi
cd resources


if [ -d "AutoPhrase" ]; then
    echo ' => AutoPhrase exists!'
else
    git clone https://github.com/shangjingbo1226/AutoPhrase
fi
cd ..


# Creating symbolic link
ln -s resources/AutoPhrase/src src
ln -s resources/AutoPhrase/tools tools
# ln -s resources/AutoPhrase/auto_phrase.sh auto_phrase.sh
ln -s resources/AutoPhrase/data data
