#!/usr/bin/python
# recommendations.py

"""
This file contains code adapted from Chapter 2 of "Programming Collective Intelligence", Making Recommendations
"""

import numpy as np
import scipy as sp

critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0,
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5,
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0,
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5,
    },
    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0,
    },
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5,
    },
    'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0,
             'Superman Returns': 4.0},
}

def sim_distance(prefs, p1, p2):
	"""
	Calculates the similarity between two actors according to Euclidean distance

	Arguments:
		prefs - dictionary, key=actor, values=dictionary of preferences per item
		p1, p2 - strings, denoting actors
	"""
	s1 = set(prefs[p1].keys())
	s2 = set(prefs[p2].keys())

	if len(s1.intersection(s2)) == 0:
		return 0
	else:
		diffs = np.array([prefs[p1][a] - prefs[p2][a] for a in s1.intersection(s2)])
		ss = np.sum(diffs**2)
		return 1/(1+ss)


def topMatches(prefs, person, n=5, similarity=sim_distance):
	"""
	Returns the top 
	"""
	scores = [(similarity(prefs,person,other),other) for other in prefs if other!=person]

	scores.sort() # sort the scores
	scores.reverse() # highest match first
	return scores[0:n]

def getRecommendations(prefs, person, similarity=sim_distance):
	"""
	Recommends items for the acotr by scoring them according to other actors' similarity
	scores.
	"""
	totals = {}
	simSums = {}
	for other in prefs:
		if other == person: continue
		else:
			sim = similarity(prefs,person,other)

		if sim <= 0: continue # ignore actors whose similarity is non-positive
		for item in prefs[other]:
			if item not in prefs[person] or prefs[person][item] == 0: # only score items the actor hasn't seen
				totals.setdefault(item,0)
				totals[item] += prefs[other][item]*sim
				simSums.setdefault(item,0)
				simSums[item] += sim

	rankings = [(total/simSums[item],item) for item,total in totals.items()] # create normalized ranking list

	rankings.sort()
	rankings.reverse()
	return rankings




