import os
import json
with open('l.json', 'r') as lg:
  login = json.load(lg)
  print()

if(login == 0): # first login installing desktop
  from installer.some import cpu
  from installer.some import save
  cpu()
  print("Hello to install tool")
  wm = input("Which wm you want(i3,xfce,kde)?: ")
  if(wm == "i3"): # i3 DE
    os.popen('sh ~/dddats/script/installer/i3.sh').read()
    save()
  if(wm == "xfce"): #xfce WM
    os.popen('sh ~/dddats/script/installer/xfce.sh').read()
    save()
  if(wm == "kde"): #kde WM
    os.popen('sh ~/dddats/script/installer/kde.sh').read()
    save()
while(login == 1):
    todo = input("What you wanna do? (drivers,sysupd,pkginstall): ")
    if (todo == "drivers"):
        wh = input("Which drivers you need?(nvidia,intel): ")
        # nvidia section
        if (wh == "nvidia"):
            from installer.some import nvidia
            nvidia()
            continue
        # intel section
        elif (wh == "intel"):
           from installer.some import intel
           intel()
           continue
    if (todo == "sysupd"):
        sure = input("(yes,no)?: ")
        if (sure == 'yes'):
            os.system('sudo xbps-install -Syu')
        else:
            continue
    if (todo == "pkginstall"):
        from installer.some import apper
        apper()
        continue
    else:
        break
