#!/bin/bash


# BASH ALIAS
# alias jay="sudo bash ~/jay.sh" [this is used to update or install. Important: this .sh script has to be set as executable]


# OpenSuse
if [ $# = 0 ]; then
    sudo zypper update &&
    sudo zypper dup &&
    sudo zypper rm -u
else
    sudo zypper install $*
fi
