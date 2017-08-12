#!/usr/bin/python
# searchengine.py

"""
Implements a basic search engine, as in chapter 4 of the text
"""

import urllib2
from bs4 import BeautifulSoup
from urlparse import urljoin
from pysqlite2 import dbapi2 as sqlite

ignorewords = set(['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it'])

class crawler:

	def __init__(self, dbname):
		self.con = sqlite.connect(dbname)

	def __del__(self):
		self.con.close()

	def dbcommit(self):
		self.con.commit()

	# Auxillary function for getting an entry id and adding
	# it if it's not present
	def getentryid(self, table, field, value, createNew=True):
		return None

	# Index an individual page
	def addtoindex(self, url, soup):
		print "Indexing %s"%url

	# Extract the text from an HTML page (no tags)
	def gettextonly(self, soup):
		return

	# Separate the words by any non-whitespace character
	def separatewords(self, text):
		return None

	# Return true if this url is already indexed
	def isindexed(self, url):
		return False

	# Add a link between two pages
	def addlinkref(self, urlFrom, urlTo, linkText):
		pass

	# Starting with a list of pages, do a breadth first search
	# to the given depth, indexing pages as we go
	def crawl(self, pages, depth=2):
		for i in range(depth):
			newpages = set()
			for page in pages:
				try:
					c = urllib2.urlopen(page)
				except:
					print "Could not open %s" % page
					continue
				soup = BeautifulSoup(c.read())
				self.addtoindex(page, soup)

				links = soup('a')
				for link in links:
					if 'href' in dict(link.attrs):
						url = urljoin(page, link['href'])
						if url.find("'") != -1: continue
						url = url.split('#')[0] # remove location portion
						if url[0:4] == 'http' and not self.isindexed(url):
							newpages.add(url)
						linkText = self.gettextonly(link)
						self.addlinkref(page, url, linkText)
				self.dbcommit()
			pages = newpages


	# Create the database tables	
	def createindextables(self):
		self.con.execute('create table urllist(url)')
		self.con.execute('create table wordlist(word)')
		self.con.execute('create table wordlocation(urlid,wordid,location)')
		self.con.execute('create table link(fromid integer,toid integer)')
		self.con.execute('create table linkwords(wordid,linkid)')
		self.con.execute('create index wordidx on wordlist(word)')
		self.con.execute('create index urlidx on urllist(url)')
		self.con.execute('create index wordurlidx on wordlocation(wordid)')
		self.con.execute('create index urltoidx on link(toid)')
		self.con.execute('create index urlfromidx on wordlist(fromid)')
		self.dbcommit()


