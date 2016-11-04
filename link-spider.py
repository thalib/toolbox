'''
A simple script of mine to scrap a website and build all the webpage/url of that site.

How to run this script
virtualenv -p python3 env
source env/bin/activate
pip install --upgrade pip
pip install requests urlparse3 urllib5 bs4

python link-spider.py -l http://google.com
'''

from bs4 import BeautifulSoup
import requests, getopt, sys
from urllib.parse import urlparse

##Global variables
master = []
working = []
webURL = 0
verifySSL = True
fd = 0
##################
###File operations
def FileOpen(filename):
	global fd
	fd = open(filename, 'w')

def FileClose():
	global fd
	fd.close()

def FileWriteLine(line):
	global fd
	fd.write(line)
	fd.write("\n")
	fd.flush()

def FileWriteList(links):
	lfd = open('links_list.txt', 'w')
	for line in links:
		lfd.write(line)
		lfd.write("\n")
	lfd.close()
	print ("Written the links to file links.txt")

###################
def getBaseURL(url):
	temp = urlparse(url)
	return temp.netloc

def parse(base_url, url, verifySSL):
	links = []
	html = requests.get(url, verify=verifySSL).content
	soup = BeautifulSoup(html, "html.parser")
	for a in soup.find_all('a', href=True):
		if ("http" in a['href']) & (base_url in a['href']):
			if not (a['href'].endswith("xml")) | ("docs" in a['href']):
				links.append(a['href'])
	return links

def appendToWorking(links):
	##Remove duplicates
	result = list(set(links))
	result.sort()
	##Add new urls to working
	count = 0
	for url in result:
		if url not in working:
			working.append(url)
			count+=1
	if(count != 0):
		print("Found", count, "New URLS")


def help():
	print (sys.argv[0] + ' <option> -l <url>')
	print ('-n Disable SSL Verfiy')
	sys.exit()

##Main script starts here


try:
	opts, args = getopt.getopt(sys.argv[1:],"nhl:")
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

##Prepare
if(0 == webURL):
	help()

baseURL = getBaseURL(webURL)
print("BaseURL:", baseURL)
working.append(webURL)
FileOpen('links.txt')
##Find all
count=1
while (True):
	for url in working:
		if url not in master:
			print("URL", len(master), '/', len(working), ":", url)
			temp = parse(baseURL, url, verifySSL)
			appendToWorking(temp)
			master.append(url)
			FileWriteLine(url)
			count += 1
	if(len(working) == len(master)):
		break


# Sort both master list and working list
list(set(master))
master.sort()
print ("\nTotal Links: ", len(master))
FileClose()
FileWriteList(master)
