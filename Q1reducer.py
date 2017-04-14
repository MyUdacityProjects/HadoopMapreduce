#!/usr/bin/python
import sys

totalSale = 0
oldKey = None

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisKey, thisSale = data
	if oldKey and oldKey != thisKey:
		print oldKey, "\t", totalSale
		oldKey = thisKey
		totalSale = 0

	oldKey = thisKey
	totalSale += float(thisSale)

if oldKey != None:
	print oldKey, "\t", totalSale
