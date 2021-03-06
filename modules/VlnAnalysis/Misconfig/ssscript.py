#!/usr/bin/env python3
# coding:  utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: 0xInfection (@_tID)
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import os
import time
import sys
import subprocess
sys.path.append('files/')
from core.Core.colors import *
from modules.VlnAnalysis.Misconfig.subdom0x00 import *

info = "This module hunts for Same Site scripting vulnerabilities."
searchinfo = "Same Site Scripting"
properties = {}

def ssscript(web):

    vuln = []
    novuln = []
    web = web.replace('https://','')
    web = web.replace('http://','')
    webb = web
    if "@" in web:
        webb = web.split("@")[1]
    #print(R+'\n   =======================================')
    #print(R+'\n    S A M E - S I T E   S C R I P T I N G')
    #print(R+'   ——·‹›·––·‹›·——·‹›·——·‹›·––·‹›·——·‹›·——·\n')
    from core.methods.print import pvln
    pvln("same-site scripting") 
                
    time.sleep(0.5)
    try:
        if os.path.exists('files/'+webb+'-subdomains.lst') == True:
            pass
        else:
            print(O+' [*] Gathering subdomains...')
            print(GR+' [*] Initializing subdomain gathering...')
            subdom0x00(web)
    except:
        print(R+' [-] Exception occured!')

    os.system('mv '+webb+'-subdomains.lst tmp/')
    #print(R+'\n    =========================')
    print(R+'\n     S - S - S   T E S T E R')
    print(R+'    ––·‹›·––·‹›·––·‹›·––·‹›·–\n')
                 
    try:
        with open('tmp/'+webb+'-subdomains.lst','r') as dom:
            for m in dom:
                m = m.replace('\n','')
                print(C+' [*] Running tests on '+GR+m+C+' for Same-Site Scripting...')
                time.sleep(1.5)
                try:
                    mp = socket.gethostbyname(m)
                    if '127.0.0.1' in mp or '0.0.0.0' in mp:
                        time.sleep(0.7)
                        print(G+' [+] This website is vulnerable to Same Site Scripting!')
                        vuln.append(web)
                    else:
                        time.sleep(0.7)
                        print(R+' [-] '+O+m+R+' is immune to Same-Site Scripting!')
                        novuln.append(web)

                except socket.gaierror:
                    time.sleep(0.7)
                    pass
    except Exception as e:
        print(R+' [-] Error occured while processing module')
        print(R+' [-] Error : '+str(e))
        pass

def attack(web):
    ssscript(web)