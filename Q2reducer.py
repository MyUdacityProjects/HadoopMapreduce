#!/usr/bin/python
import sys

salesMax = 0
oldKey = None

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisKey, thisSale = data
	if oldKey and oldKey != thisKey:
		print oldKey, "\t", salesMax
		oldKey = thisKey
		salesMax = 0

	oldKey = thisKey
	if float(thisSale) > salesMax:
		salesMax = float(thisSale)

if oldKey != None:
	print oldKey, "\t", salesMax
