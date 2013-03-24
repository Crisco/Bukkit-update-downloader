#!/usr/bin/env python
import sys

try:
	from urllib import urlretrieve
except ImportError:
	from urllib.request import urlretrieve

from os import getcwd

#Prints the current progress when downloading
def Progress(current, blockSize, total):
	percent = int((current*blockSize*100)/total) #Takes number of blocks downloaded multiplies it by size and 100 then divides by total size to get an integer value
	sys.stdout.write("\rPercent Done: %2d%%\r" % percent)
	sys.stdout.flush()

def downloadFile(type): #downloads the dev and beta crafbukkit versions
	print("Downloading \"craftbukkit-"+type+".jar\" to " + getcwd())
	urlretrieve("http://dl.bukkit.org/latest-"+type+"/craftbukkit-"+type+".jar", "craftbukkit-"+type+".jar", reporthook=Progress)
	print("\nDone!")

if len(sys.argv)<2:
	print("USAGE: update-bukkit <rel,beta,dev>")
elif sys.argv[1]=="rel": #since the release bukkit format is very different from the other two I just hardcoded it
	print("Downloading \"craftbukkit.jar\" to " + getcwd())
#	urlretrieve("http://dl.bukkit.org/latest-rb/craftbukkit.jar", "craftbukkit.jar", reporthook=Progress)
	urlretrieve("https://dl.dropbox.com/u/5135448/screenshot.png", "test.png", reporthook=Progress)
	print("\nDone!")
elif sys.argv[1]=="dev" or sys.argv[1]=="beta":
	downloadFile(str(sys.argv[1]))
else:
	print("USAGE: update-bukkit <rel,beta,dev>")

