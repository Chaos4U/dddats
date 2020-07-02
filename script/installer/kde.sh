#!/bin/sh

# xorg
sudo xbps-install -Syu
sudo xbps-install -Sy xorg

# kde
sudo xbps-install -Sy kde5 kde5-baseapps

# dm
sudo xbps-install -Sy lightdm lightdm-gtk3-greeter
sudo ln -s /etc/sv/dbus /var/service/dbus
sudo ln -s /etc/sv/lightdm /var/service/lightdm
