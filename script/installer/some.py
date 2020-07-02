login = 0

import os

def nvidia():
    need = input("You really want to install nvidia drivers?(yes,no): ")
    if (need == 'yes'):
        print("Which version? (nvidia390,nvidia) 390 for 300/400 series. when nvidia 500+")
        v = input()
        if (v == 'nvidia'):
            os.system('sudo xbps-install -S nvidia')
        if (v == 'nvidia390'):
            os.system('sudo xbps-install -S nvidia390')
        else:
            print("Something went wrong!")
    else:
        print("Nothing to do!")
def intel():
      need = input("You really want to install intel drivers?(yes,no): ")
      if (need == 'yes'):
        os.system('sudo xbps-install -S linux-firmware-intel mesa-dri')
      else:
        print('You said no, or something else!')
      accel = input('Do you need video accel?(if yes, type i965,iHD): ')
      if (accel == 'i965'):
        os.system('sudo xbps-install -S libva-intel-driver')
      if (accel == 'iHD'):
        os.system('sudo xbps-install -S intel-media-driver')
      else:
        print('Nothing to do!')
def apper():
    print('''Hey, i know only few pkgs.
    All of this (Case sensetive)
    Type the name of section. Example - Browsers.And lutris = Lutris
    Lutris(app for games)
    Browsers(Firefox,Chromium)
    File manager(pcmanfm,thunar)
    Audio("drivers") (alsa,pulseaudio)
    And i can try to install your app,program''')
    what = input("What you want?:")
    if (what == 'Lutris'):
        os.system('sudo xbps-install -S lutris')
    elif (what == 'Browsers'):
        which = input("Which browser you want?: ")
        if (which == 'Firefox'):
            os.system('sudo xbps-install -S firefox')
        elif (which == 'Chromium'):
            os.system('sudo xbps-install -S chromium')
    elif (what == 'File manager'):
        which = input("Which file manager you want?: ")
        if (which == 'pcmanfm'):
            os.system('sudo xbps-install -S pcmafm')
        elif (which == 'thunar'):
            os.system('sudo xbps-install -S Thunar')
    elif (what == "Audio"):
        print('Alsa may not work, because it "Beta" ')
        which = input("Which audio driver you would use?: ")
        if (which == 'pulseaudio'):
            os.system('sudo xbps-install -S pulseaudio')
        elif (which == 'alsa'):
            os.system('sudo xbps-install -S alsa')
    elif (len(what) > 0):
        whate = input("What you want try to install?: ")
        os.system('sudo xbps-install -S ' + whate)
def cpu():
    wha = input("Which cpu you using. (amd, intel): ")
    if (wha == 'amd'):
        os.system('sudo xbps-install -Sy linux-firmware-amd')
    if (wha == 'intel'):
        os.system('sudo xbps-install -Sy intel-ucode')
