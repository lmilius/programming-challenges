#!/usr/bin/python
numGiven=7
numQueries=2
givenNumbers = [21, 9, 5, 8, 10, 1, 3]
queryNumbers = [10, 15]

def removeGtEq(query):
	count = 0
	for num in givenNumbers:
		if query <= num:
			count += 1
	return count

print removeGtEq(queryNumbers[0])

