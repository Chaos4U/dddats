#!/bin/sh

# xorg
sudo xbps-install -Su
sudo xbps-install -S xorg

# kde
sudo xbps-install -S kde5 kde5-baseapps
