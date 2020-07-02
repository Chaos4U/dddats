import os

# base
os.system('sudo xbps-install -Syu')
os.system('sudo xbps-install -Sy xorg')

# i3 install
os.system('sudo xbps-install -Sy i3status dmenu nano sakura')

# i3 background
os.system('sudo xbps-install -Sy feh')


# some apps
os.system('sudo xbps-install -Sy lxappearance')
os.system('sudo xbps-install -Sy papirus-icon-theme')
os.system('sudo xbps-install -Sy arc-theme')
os.system('sudo xbps-install -Sy mousepad')

os.system('sudo xbps-install -Sy lightdm lightdm-gtk3-greeter')
os.system('sudo ln -s /etc/sv/dbus /var/service/dbus')
os.system('sudo ln -s /etc/sv/lightdm /var/service/lightdm')



