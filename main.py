#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:46:00 2023

@author: amir
"""

from extractor import get_url,request_site,crawler,view_result,write_disk

class Handler:
    
    def run():
        url = get_url()
        site = request_site(url)
        music = crawler(site)
        view_result(music)
        write_disk(mp3_link=music)
        
        
        


if __name__ == "__main__":
    Handler.run()