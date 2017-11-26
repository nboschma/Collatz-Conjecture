#! python

import sys
sys.stdout.write("hello form python %s\n" % (sys.version,))

import math

def collatzodd(number):
	return (3*number+1)/2

def collatzeven(number):
	return (number/2)

def collatz(number):
	while(number > 1):
		if(number % 2 == 0):
			number = collatzeven(number)
		else:
			number = collatzodd(number)


for x in range(0, 999999):
	collatz(x)
	print ("collatz conjecture holds for x=%d" % x)