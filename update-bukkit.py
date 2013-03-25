#!/usr/bin/env python
import sys

try:
	from urllib import urlretrieve
except ImportError:
	from urllib.request import urlretrieve

try:
	from urllib import urlopen
except ImportError:
	from urllib.request import urlopen

import hashlib
import re
from os import getcwd

#Prints the current progress when downloading
def Progress(current, blockSize, total):
	percent = int((current*blockSize*100)/total) #Takes number of blocks downloaded multiplies it by size and 100 then divides by total size to get an integer value
	sys.stdout.write("\rPercent Done: %2d%%\r" % percent)
	sys.stdout.flush()

def isUpToDate(version):
	if version != "rel":
		pageSource=urlopen("http://dl.bukkit.org/downloads/craftbukkit/list/"+version+"/").read() #Downloads the correct bukkit information page
		version = "-" + version		
	else:
		pageSource=urlopen("http://dl.bukkit.org/downloads/craftbukkit/list/rb/").read()
		version = ""
	try: #tries to open the craftbukkit<version>.jar. If it exists it will continue checking to see if it is updated, if not then it will download the latest version
		downloaded = open("craftbukkit"+version+".jar", 'rb')
	except IOError:
		return False
	dMD5 = hashlib.md5(downloaded.read()).hexdigest() #calculates the md5sum of the current file
	nMD5 = re.search(b"<dt>MD5 Checksum:</dt>.*?</dd>", pageSource, re.DOTALL) #uses regex to search the webpage for the latest md5sum
	nMD5 = re.search(b"(?<= )[0-9a-z].*?\n", nMD5.group(0))
	nMD5 = nMD5.group(0).rstrip()
	print("Latest Version: "+nMD5.decode("utf-8")+"\nYour Version: "+dMD5)
	if nMD5.decode("utf-8")==dMD5: #compares the two sums. If the current file is up to date, it won't do anything else.
		return True
	else:
		return False


def downloadFile(type): #downloads the dev and beta crafbukkit versions
	if isUpToDate(type)==False:
		if type != "rel":
			print("Downloading \"craftbukkit-"+type+".jar\" to " + getcwd())
			urlretrieve("http://dl.bukkit.org/latest-"+type+"/craftbukkit-"+type+".jar", "craftbukkit-"+type+".jar", Progress)
			print("\nDone!")
		else:	
			print("Downloading \"craftbukkit.jar\" to " + getcwd())
			urlretrieve("http://dl.bukkit.org/latest-rb/craftbukkit.jar", "craftbukkit.jar", Progress)
			print("\nDone!")
	else:
		print("You are already up to date!")

if len(sys.argv)<2:
	print("USAGE: update-bukkit <rel,beta,dev>")
elif sys.argv[1]=="dev" or sys.argv[1]=="beta" or sys.argv[1]=="rel":
	downloadFile(str(sys.argv[1]))
else:
	print("USAGE: update-bukkit <rel,beta,dev>")

