#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import os
import time
from core.methods.tor import session
import urllib.parse
from core.Core.colors import *

info = "Apache server status hunter."
searchinfo = "Apache Status Hunter"
properties = {}

def apachestat(web):
    requests = session()
    flag = 0x00
    print(GR+' [*] Loading module...')
    time.sleep(0.7)
    #print(R+'\n    ===========================')
    #print(R+'     A P A C H E   S T A T U S ')
    #print(R+'    ===========================\n')

    from core.methods.print import posintact
    posintact("apache status") 

    print(C+' [*] Importing fuzz parameters...')
    time.sleep(0.7)
    print(GR+' [*] Initializing bruteforce...')
    with open('files/fuzz-db/apachestat_paths.lst','r') as paths:
        for path in paths:
            path = path.replace('\n','')
            url = web + path
            print(B+' [+] Trying : '+C+url)
            resp = requests.get(url, allow_redirects=False, verify=False, timeout=7)
            if resp.status_code == 200 or resp.status_code == 302:
                print(O+' [+] Apache Server Status Enabled at :'+C+color.TR3+C+G+url+C+color.TR2+C)
                flag = 0x01

    if flag == 0x00:
        print(R+' [-] No server status enabled!')
    print(C+' [+] Apache server status completed!\n')

def attack(web):
    apachestat(web)