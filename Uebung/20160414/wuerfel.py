from random import randint

# 1000 wuerfe, augensumme wird im array gespeichert und zurueckgegeben
def wuerfeln():
	result = {}
	for x in range(1000):
		rdmOne = randint(1,6)
		rdmTwo = randint(1,6)
		result[x] = rdmOne + rdmTwo
		#print(result[x])
	return result

# haeufigkeit der augensummen zaehlen
def count(wuerfelArray):
	countResult = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for y in wuerfelArray:
		summe = wuerfelArray[y] -1
		#print(summe)
		countResult[summe] += 1
	return countResult

# ausgabe
def printResult(countArray):
	for x in countArray:
		print(x)


wuerfelResult = wuerfeln()
countResult = count(wuerfelResult)
printResult(countResult)