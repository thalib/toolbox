#!env3/bin/python

'''
A simple script of mine to pull the webpage/url save to markdown file

url2markdown2.py is rewrite of v1, using newspaper library: http://newspaper.readthedocs.io

How to run this script
virtualenv -p python3 env3
source env3/bin/activate
pip install -r requirements.txt


python pul-pagepy -l http://example.com/url.html
'''

import requests
import getopt
import sys
import os
import html2text
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import urllib.request
import re
import newspaper
import yaml


def help():
    print (sys.argv[0] + ' <file.md>')
    sys.exit()


def getBaseURL(url):
    temp = urlparse(url)
    return temp.netloc

############
webURL = 0
verifySSL = 0
BaseURL = 0

try:
    opts, args = getopt.getopt(sys.argv[1:], "h")
except getopt.GetoptError:
    help()
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        help()
    else:
        assert False, "unhandled option"

# webURL = args[0]
# if(0 == webURL):
#    help()

documents = """
---
name: The Set of Gauntlets 'Pauraegen'
description: >
    A set of handgear with sparks that crackle
    across its knuckleguards.
---
name: The Set of Gauntlets 'Paurnen'
description: >
    A set of gauntlets that gives off a foul,
    acrid odour yet remains untarnished.
---
name: The Set of Gauntlets 'Paurnimmen'
description: A set of handgear, freezing with unnatural cold.
...

Suppoer duper 
"""

print(documents)

for data in yaml.load_all(documents):
    print (data)
