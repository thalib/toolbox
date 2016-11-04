'''
A simple script of mine to pull the webpage/url save to markdown file

How to run this script
virtualenv -p python3 env
source env/bin/activate
pip install --upgrade pip
pip install requests urlparse3 urllib5 bs4 html2text

python pul-pagepy -l http://example.com/url.html
'''

import requests
import getopt
import sys, os
import html2text
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import urllib.request

def help():
    print (sys.argv[0] + ' <option> -l <url>')
    print ('-n Disable SSL Verfiy')
    sys.exit()


def getURL(url, verifySSL):
    req = requests.get(url, verify=verifySSL).content
    return req

def run_command(cmd):
	print (cmd)
	ret = os.system(cmd)
	if 0 == ret:
		print ('PASS: ' + cmd)
	else:
		sys.exit('ERROR: ' + cmd)
	print('***********************************************************')

############
webURL = 0
verifySSL = 0

try:
    opts, args = getopt.getopt(sys.argv[1:], "nhl:")
except getopt.GetoptError:
    help()
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        help()
    elif opt == '-l':
        webURL = arg
    elif opt == '-n':
        verifySSL = False

if(0 == webURL):
	help()


'''
Read from file
html = open("index.html").read()
out = html2text.html2text(html)
print(html)
'''
try:
    url = urllib.request.urlopen(webURL)
    html = url.read()
except Exception as inst:
    print('Try to download the page with wget')
    cmd = 'wget -O temp.html ' + webURL
    run_command(cmd)
    html = open("temp.html").read()

soup = BeautifulSoup(html, 'html.parser')
data = html2text.html2text(soup.prettify())

fd = open('post.md', 'w')

if (soup.title):
    fd.write("Title: ")
    fd.write(soup.title.string)
    fd.write("\n")

fd.write("URL: ")
fd.write(webURL)
fd.write("\n")
fd.write(data)
fd.write("\n")
fd.close()
