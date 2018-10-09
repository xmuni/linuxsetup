#!/bin/bash

# ADD BASH ALIASES
sudo echo "alias upd='sudo apt update -yy'" >> ~/.bashrc
sudo echo "alias upg='sudo apt upgrade -yy'" >> ~/.bashrc
echo "- Bash aliases set up"

# COPY ALL FONTS TO THE FONTS FOLDER
sudo cp -R fonts/* /usr/share/fonts
echo "- Fonts installed"

# ADD ASTERISK TO TERMINAL PASSWORD
# sed -i 's/before/after/g' file.txt
sudo sed -i 's/env_reset/env_reset,pwfeedback/g' /etc/sudoers
echo "- Added asterisks for terminal password input"