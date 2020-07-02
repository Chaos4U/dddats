#!/bin/sh

# base
sudo xbps-install -S xorg

# i3 install
sudo xbps-install -Su
sudo xbps-install -S i3status dmenu nano sakura
# i3 background
sudo xbps-install -S feh

# some apps
sudo xbps-install -S lxappearance
sudo xbps-install -S papirus-icon-theme
sudo xbps-install -S arc-theme
sudo xbps-install -S mousepad
