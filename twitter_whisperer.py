from bs4 import BeautifulSoup as soupy
import urllib.request
import re
import subprocess
import sys
import os

html = urllib.request.urlopen("https://twitter.com/<Your Account Here>").read()
soup = soupy(html, "lxml")

x = soup.find("meta", {"name": "description"})['content']
command = re.findall('"([^"]*)"', x)

def panic():

    print("Shutting down")

    if "win" in sys.platform:
        os.popen("shutdown /p /f")
    elif "darwin" in sys.platform:
        os.popen("shutdown -s now")
    elif "linux" in sys.platform or "bsd" in sys.platform:
        os.popen("poweroff")

    if "win" in sys.platform:
        os.popen("truecrypt /d")
    else:
        os.popen("truecrypt -d")


if command[0] == "panic":
    panic()
else:
    subprocess.call(command[0])

