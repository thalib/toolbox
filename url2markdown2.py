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


def help():
    print (sys.argv[0] + ' <url>')
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

webURL = args[0]

if(0 == webURL):
    help()

print ('Fetching: ' + webURL)

try:
    article = newspaper.Article(
        webURL, fetch_images=False, keep_article_html=True)
except:
    print("Error when getting article info")
    sys.exit(2)

try:
    article.download()
except:
    print("Failed when downloading")
    sys.exit(2)

try:
    article.parse()
except:
    print("Error during parsing article")
    sys.exit(2)


#soup = BeautifulSoup(article.article_html, 'html.parser')
#soup.find('div', id="header").decompose()

data = html2text.html2text(article.article_html)

# print(article.text)
# print(article.title)


print ('Writing to post.md')

fd = open('post.md', 'w')

if (article.title):
    fd.write(article.title)
    fd.write("\n\n")

baseURL = getBaseURL(webURL)
viaURL = 'via [' + baseURL + '](' + webURL + ')'

if (article.movies):
    fd.write("Video")
    fd.write(",".join([str(x) for x in article.movies]))
    fd.write("\n\n")

if (article.top_image):
    fd.write("![%s](", article.title)
    fd.write(article.top_image)
    fd.write(")\n\n")


fd.write(data)
fd.write("\n")

fd.write(viaURL)
fd.write("\n")


fd.close()
