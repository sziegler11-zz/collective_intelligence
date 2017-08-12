#!/usr/bin/python
# searchengine.py

"""
Implements a basic search engine, as in chapter 4 of the text
"""

class crawler:

	def __init__(self, dbname):
		pass

	def __del__(self):
		pass

	def dbcommit(self):
		pass

	# Auxillary function for getting an entry id and adding
	# it if it's not present
	def getentryid(self, table, field, value, createNew=True):
		return None

	#Index an individual page
	def addtoindex(self, url, soup):
		print "Indexing %s"%url

	# Extract the text from an HTML page (no tags)
	def getextonly(self, soup):
		return

	# Separate the words by any non-whitespace character
	def separatewords(self, text):
		return None