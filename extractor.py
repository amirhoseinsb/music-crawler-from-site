#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 22:00:53 2023

@author: amir
"""

import requests 
import re
from bs4 import BeautifulSoup


def get_url():
    url = input(str('ENTER URL : '))
    return url

def request_site(site_url):
    session = requests.session()
    session.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36'})
    html_page = session.get(url=site_url)
    return html_page

def crawler(html_page):
    music = set()
    string = html_page.text
    pattern = r"""([https+\:\/\/[a-zA-Z0-9\/\.\-\_\!\@\#\$\%\^\&\*\(\)]+\.mp3)"""
    regex = re.findall(pattern,string)
    
    if len(regex) !=0:
        for link in regex :
            music.add(link)
        return music
    
    else:
        return "LINK NOT FOUND !"
                            

def view_result(music):
    counter = 1
    music = music
    for link in music:
        #print(f'\n{counter} : {link}')
        #counter +=1
        print(f'{link}\n')
def write_disk(mp3_link):
    mp3_link = mp3_link
    file = open('./music/file.txt','w')
    for data in mp3_link:
        file.write(f'{data}\n')
        























