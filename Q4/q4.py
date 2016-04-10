#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#	EXECUÇÃO!
#	Requirements:
#	1) To run the following code, you must have Python 2.7 installed.
#	2) You need to install pip: $ sudo apt-get install python-pip
#	3) Install bs4: $ apt-get install python-bs4
#	4) Install BeautifulSoup: $ pip install beautifulsoup4
#	5) In case of upgrade error, run the command: $ sudo pip install --upgrade beautifulsoup4 
#	6) Install requests: $ sudo pip install requests
#	7) To execute the script: Step1) Go to terminal, Step2) Go to the script folder and run the following command: python q4.py
#	ENJOY! =) =)
#

from bs4 import BeautifulSoup as bs
import urllib2
from lxml import html

url="http://www.submarino.com.br/"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

req = urllib2.Request(url, headers=headers)

print '#'*144

#getting the best seller name
soup = bs(urllib2.urlopen(req))
title = soup.find(attrs={"class": "prodTitle"})['title']
print "Mais comprado: " + title

#getting its price
for inter in soup.find(attrs={"class": "product-price-integer"}):
	for deci in soup.find(attrs={"class": "product-price-decimal"}):
			print "Preco: " + (inter.string).replace(" ", "")+deci.string

print '#'*144