#!/bin/sh

# base
sudo xbps-install -Syu
sudo xbps-install -Sy xorg

# i3 install
sudo xbps-install -Sy i3 i3status dmenu nano sakura

# i3 background
sudo xbps-install -Sy feh


# some apps
sudo xbps-install -Sy lxappearance
sudo xbps-install -Sy papirus-icon-theme
sudo xbps-install -Sy arc-theme
sudo xbps-install -Sy mousepad

sudo xbps-install -Sy lightdm lightdm-gtk3-greeter
sudo ln -s /etc/sv/dbus /var/service/dbus
sudo ln -s /etc/sv/lightdm /var/service/lightdm



