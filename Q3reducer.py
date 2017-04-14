#!/usr/bin/python
import sys

totalSale = 0.0
saleCount = 0

for sale in sys.stdin:
	totalSale += float(sale)
	saleCount += 1

print totalSale, "\t", saleCount
