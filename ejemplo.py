# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:50:42 2021

@author: usuario
"""

def isYearLeap(año):
	#return not (año % 4)
    #return not not  (año % 100 )
    return not (año % 400)
isYearLeap (2000)




año = 2016

print("Es bisiesto" if not año % 4 and (año % 100 or  not año % 400) else "No es bisiesto")
testData = [1900, 2000, 2016, 1987]

testResults = [False, True, True, False]

for i in range(len(testData)):

            yr = testData[i]

            print(yr,"->",end="")

            result = isYearLeap(yr)

            if result == testResults[i]:

                        print("OK")

            else:

                        print("Failed")