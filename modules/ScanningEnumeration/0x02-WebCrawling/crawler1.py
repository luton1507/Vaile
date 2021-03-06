#!/usr/bin/env python3
# -*- coding : utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import os
#import requests
from core.methods.tor import session
import core.lib.mechanize as mechanize
import http.cookiejar
from urllib.request import urlparse
import time
from time import sleep
from core.Core.colors import *
from core.variables import tor

br = mechanize.Browser()

cj = http.cookiejar.LWPCookieJar()
br.set_cookiejar(cj)

br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

torproxies = {'http':'socks5h://localhost:9050', 'https':'socks5h://localhost:9050'}
if tor:
    br.set_proxies(torproxies)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [
    ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

linksall = []
cis = []
crawled = []

info = "Depth 1 Crawler."
searchinfo = "Depth 1 Crawler"
properties = {}

def crawler10x00(web):
    requests = session()
    time.sleep(0.5)
    #print(R+'\n    ===========================')
    #print(R+'     C R A W L E R  (Depth 1)')
    #print(R+'    ==========================\n')
    from core.methods.print import pscan
    pscan("crawler (depth 1)")
    print(C+' [This module will fetch all links')
    print(C+' from an online API and then crawl ')
    print(C+'         them one by one]      ')
    time.sleep(0.4)
    print(''+GR+' [*] Parsing the web URL... ')
    time.sleep(0.3)
    print('' +B+ ' [!] URL successfully parsed...')
    print('' + GR+ ' [*] Getting links...')
    time.sleep(0.4)
    text = requests.get('http://api.hackertarget.com/pagelinks/?q=' + web).text
    lol = str(text)
    linksall = lol.splitlines()
    for m in linksall:
        if 'http' in m and 'https' not in m:
            cis.append(m)

    flag = 0x00
    for x in cis:
        try:
            print(O+' [+] Crawling link :>'+ C+color.TR3+C+G + str(x)+C+color.TR2+C)
            br.open(x)
            flag = 0x01
            crawled.append(x)

        except Exception as e:
            print(R+' [-] Exception : '+str(e)+'\n')

    if flag == 0x00:
        print(R+' [-] Unable to find any links...')
        print(C+' [+] Please use the second crawler... :)')

    return crawled

def out(web, list0):

    web = web.split('//')[1]
    print(GR+' [*] Writing found URLs to a file...')
    if os.path.exists('tmp/logs/'+web+'-logs/'+web+'-links.lst'):
        fil = open('tmp/logs/'+web+'-logs/'+web+'-links.lst','w+')
        print(P+' [!] Sorting only scope urls...'+C)
        time.sleep(1)
        for lists in list0:
            if str(web) in lists:
                fil.write("%s\n" % lists)
        mq = os.getcwd()
        print(O+' [+] Links saved under'+C+color.TR3+C+G+mq+'tmp/logs/'+web+'-logs/'+web+'-links.lst'+C+color.TR2+C)

    else:
        fil = open('tmp/logs/'+web+'-logs/'+web+'-links.lst','a')
        print(C+' [!] Sorting only scope urls...')
        time.sleep(1)
        for lists in list0:
            if str(web) in lists:
                fil.write("%s\n" % lists)
        mq = os.getcwd()
        print(O+' [+] Links saved under'+C+color.TR3+C+G+mq+'tmp/logs/'+web+'-logs/'+web+'-links.lst'+C+color.TR2+C)

def crawler1(web):

    print(GR+' [*] Loading crawler...')
    time.sleep(0.5)
    q = crawler10x00(web)
    out(web, q)
    print(G+' [+] Done!'+C+color.TR2+C)

def attack(web):
    crawler1(web)