import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "Welcome to HomeNET Surveilance"
line2 = "This is the python script that will be used to organize addon windows,"
line3 = "message boxes and will arrange spawning apps within the kodi app itself."
line4 = " "
line5 = "This addon is far from finished, but stay tuned."

xbmcgui.Dialog().ok(addonname, line1, line2, line3, line4, line5)
