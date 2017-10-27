#!/usr/bin/python

# input comes in like this:
# 7 2
# 21 9 5 8 10 1 3
# 10 15

# output like this:
# 4 2

numGiven=7
numQueries=2
givenNumbers = [21, 9, 5, 8, 10, 1, 3]
queryNumbers = [10, 15]

def findRemainingCannibals(query, numArray):
	count = 0
	while len(numArray) > 0:
		maxNumber = max(numArray)
		numArray.remove(maxNumber)
		if maxNumber >= query:
			count += 1
			continue
		while maxNumber < query:
			if len(numArray) == 0: 
				break
			numArray.remove(min(numArray))
			maxNumber += 1
			if maxNumber == query:
				count += 1
				break

	return count	

def findCannibalNumbers():
	countList = []
	for query in queryNumbers:
		numberArray = list(givenNumbers)
		countList.append(findRemainingCannibals(query, numberArray))
	print countList


findCannibalNumbers()
