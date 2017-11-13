# -*- coding: UTF-8 -*-

import urllib
import webbrowser

import re

# requests is a python lib used for http level data communication
import requests

#BeautifulSoup is a good html parser to help cawler to get wanted data in a easy way
from bs4 import BeautifulSoup

url_set = set()
key_word_set = set()

#note: if uisng r, return normal string; if using rb, return binary.  It will impact the following string processing.
#note: if there is Chinese (non-English) characters in data.txt, we need explicitly assign encoding = utf-8 here
#note: for each line, when we save it in the list, we'd better remove the line return cahracter - \n, otherwise it may cause trouble later
data_file = open("/users/feiqizhang/desktop/gitsmart/mac-plist/data.txt", "r", encoding = "UTF-8")

break_line = 0

#please check the format used in data.txt
for line in data_file:
	#print (line[0])
	if(break_line == 0 and line[0] == "*"):
		break_line = 1

	if (break_line == 0 and line[0] != "*"):
		url_set.add(line.strip("\n"))
	
	if (break_line == 1 and line[0] != "*"):
		key_word_set.add(line.strip("\n"))

data_file.close()



for url in url_set:
	#print (url)
	page = requests.get(url)
	soup = BeautifulSoup(page.text,"lxml")

	for key_word in key_word_set:
		#print(key_word)
		find = soup.find_all('a',text=re.compile(key_word))
		#print(find)	
		for link in find:	
			#print(link.get('href'))	
			webbrowser.open_new_tab(link.get('href'))

