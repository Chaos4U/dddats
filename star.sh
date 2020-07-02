#!/bin/sh

sudo xbps-install -Sy python3

echo "install started!"

python3 script/install.py
