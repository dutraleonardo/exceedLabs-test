#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#	1)To execute the script: Step1) Go to terminal, Step2) Go to the script folder and run the following command: python q3.py
#	ENJOY! =)
#

ts = {7,-10,13,8,4,-7.2,-12,-3.7,3.5,-9.6,6.5,-1.7,-6.2,7}

def closestToZero():	
	if len(ts) == 0:
		print '0'
	else:
		myNumber = 0
		nearZero = min(ts, key=lambda x:abs(x-myNumber))
		print nearZero
closestToZero()