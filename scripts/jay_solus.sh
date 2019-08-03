#!/bin/bash


# BASH ALIAS
# alias jay="sudo bash ~/jay.sh" [this is used to update or install. Important: this .sh script has to be set as executable]


# Solus
if [ $# = 0 ]; then
    sudo eopkg update
else
    sudo eopkg install $*
fi
