#!/usr/bin/python

#Importing request module & importing Beautisoup module from bs4
#---------------------------------------------------------------

import commands,requests,time
from bs4 import BeautifulSoup
from tqdm import tqdm
#Getting input from user
#-----------------------
search=raw_input("Enter the video name:")
url="https://www.youtube.com/results?search_query={}".format(search)
# Getting content from searched url
# ---------------------------------
r = requests.get(url)
soup = BeautifulSoup(r.content)
links = soup.find_all("a")

#Define list
#-----------
data=[]
result=[]
#Storing href link in list
#-------------------------
for link in links:
	x="<a href='%s'>"%(link.get("href"))
	if "<a href='/watch?v=" in x:
		data.append(x)
# Sorting the link and split the content to get the '/watch?v='
# -------------------------------------------------------------

for item in range(0,len(data),2):
	v = data[item].split("'")
	y = "https://www.youtube.com{}".format(v[1])
	result.append(y)
# Printing youtube watchable link 
# -------------------------------
print "-----------------------------"
print "-----------------------------"
print "-----------------------------"
print "-----------------------------"
print "----Choose Video Quality-----"
print "-------Press 1 [240p]--------"
print "-------Press 2 [480p]--------"
print "-------Press 3 [720p]--------"
n=raw_input("Enter choice: ")
print "-----------------------------"
print "please wait...."
l=result[0]
if n == '1':
	o=(commands.getstatusoutput('youtube-dl -f 17 {}'.format(l)))
elif n == '2':
        o=(commands.getstatusoutput('youtube-dl -f 18 {}'.format(l)))
elif n == '3':
        o=(commands.getstatusoutput('youtube-dl -f 22 {}'.format(l)))
else:
        print ("Wrong input ")

print "-----------------------------"
time.sleep(8)
print "Please wait..."
time.sleep(9)
print "[youtube] : Downloading Webpage"
time.sleep(15)
print "[youtube] : Downloading video info webpage"
time.sleep(15)
print "[youtube] : Extracting video information"
time.sleep(14)
print "[youtube] : Downloading MPD manifest"
time.sleep(8)
print "fetching details..."
time.sleep(9)
print "Connected to www.youtube.com"
time.sleep(15)
print "Starting Downloading..."

check = (o[1].split(" "))[-5]
if check == '100%':
        for i in tqdm(range(int(9e6))):
		pass
else:
	"Not Downloaded"



