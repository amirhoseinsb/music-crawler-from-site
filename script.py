#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 23:54:35 2023

@author: amir
"""


import requests 
import re
import sys
counter = 0

url = input(str("ENTER URL :"))
session = requests.session()
session.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36'})
html_page = session.get(url)

# pattern = r"""((http|https)+\:\/\/[a-zA-Z0-9\/\.\-\_\!\@\#\$\%\^\&\*\(\)]+\.mp3)"""
pattern = r"""([https+\:\/\/[a-zA-Z0-9\/\.\-\_\!\@\#\$\%\^\&\*\(\)]+\.mp3)"""

music = set()

string = html_page.text

regex = re.findall(pattern,string)

if len(regex) !=0:
    for link in regex :
        music.add(link)

else:
    print( "LINK NOT FOUND !")
    sys.exit()
    

for link in music:
    print(f'\n{counter} : {link}')
    counter +=1
