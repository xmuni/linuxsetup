#!/bin/bash

sudo apt install caja nomacs qbittorrent rawtherapee gimp dconf-editor gmusicbrowser krita darktable libreoffice gimp grsync dropbox-nautilus

# INSTALL SUBLIME TEXT
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-get install apt-transport-https
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt update
sudo apt install sublime-text