#!/bin/sh

sudo xbps-install -Sy
sudo xbps-install -Sy python3

echo "install started!"
sudo xbps-install -Su

python3 script/install.py
