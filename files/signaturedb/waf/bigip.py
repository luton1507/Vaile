#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# Author: @_tID (Modified version from wascan)
# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile

from re import search, I


def bigip(headers, content):
    detect = False
    for header in headers.items():
        detect |= header[0].lower() == "x-cnection"
        detect |= header[0].lower() == "x-wa-info"
        detect |= search(r'\ATS\w{4,}=|bigip|bigipserver|\AF5\Z', header[1], I) is not None
        if detect: break
    if detect:
        return "BIG-IP Application Security Manager (F5 Networks)"
