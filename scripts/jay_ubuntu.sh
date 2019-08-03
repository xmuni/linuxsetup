#!/bin/bash


# BASH ALIAS
# alias jay="sudo bash ~/jay.sh" [this is used to update or install. Important: this .sh script has to be set as executable]


# Ubuntu
if [ $# = 0 ]; then
    sudo apt update &&
    sudo apt upgrade
else
    sudo apt install $*
fi
