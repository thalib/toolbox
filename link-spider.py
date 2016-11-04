from bs4 import BeautifulSoup
import requests, getopt, sys
from urllib.parse import urlparse

'''
How to run this scriptp
virtualenv -p python3 env
cd env
source bin/activate
pip install requests urlparse3 urllib2 bs4
pip install
'''
##Global variables
master = []
working = []

def getBaseURL(url):
	temp = urlparse(url)
	return temp.netloc

def parse(base_url, url):
	links = []
	html = requests.get(url, verify=True).content
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

def writeFile(links):
	fd = open('links.txt', 'w')
	for line in links:
		fd.write(line)
		fd.write("\n")
	fd.close()
	print ("Written the links to file links.txt")

def help():
	print (sys.argv[0] + ' -l <url>')
	sys.exit()

##Main script starts here
webURL = 0
try:
	opts, args = getopt.getopt(sys.argv[1:],"hl:")
except getopt.GetoptError:
	help()
	sys.exit(2)

for opt, arg in opts:
	if opt == '-h':
		help()
	elif opt == '-l':
		webURL = arg

##Prepare
if(0 == webURL):
	help()

baseURL = getBaseURL(webURL)
print("BaseURL:", baseURL)
working.append(webURL)

##Find all
count=1
while (True):
	for url in working:
		if url not in master:
			print("URL", len(master), '/', len(working), ":", url)
			temp = parse(baseURL, url)
			appendToWorking(temp)
			master.append(url)
			count += 1
	if(len(working) == len(master)):
		break


# Sort both master list and working list
list(set(master))
master.sort()
print ("\nTotal Links: ", len(master))
writeFile(master)
