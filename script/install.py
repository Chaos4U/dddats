import os
from installer.some import login
from time import sleep

if(login == 0): # first login installing desktop
  from installer.some import cpu
  cpu()
  print("Hello to install tool")
  wm = input("Which wm you want(i3,xfce,kde)?: ")
  if(wm == "i3"): # i3 DE
    os.popen('sh ~/dddats/script/installer/i3.sh')
    sleep(20)
    login = 1
  if(wm == "xfce"): #xfce WM
    os.popen('sh ~/dddats/script/installer/xfce.sh')
    sleep(20)
    login = 1
  if(wm == "kde"): #kde WM
    os.popen('sh ~/dddats/script/installer/kde.sh')
    sleep(20)
    login = 1
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
