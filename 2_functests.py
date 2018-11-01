import math
import unittest
aBigList = [22,55,20,26,89,61,60,13,63,4,45,68,83,74,91,2,85,19,73,24,43,69,82,46,44,61,56,38,5,63,51,30,8,20,35,39,11,9,22,37,12,69,8,88,52,42,48,30,65,64,93,4,64,82,81,17,78,24,96,81,6,96,71,43,33,78,29,52,41,76,98,92,89,2,77,22,31,33,62,27,89,35,90,95,23,20,46,29,95,30,33,45,7,27,35,98,70,66,72,7]


def maxLoss(pricelist):
    if (len(pricelist) == 0):
        return 0
    
    maxIndex = maxVal = minVal = 0
    for i in range(0, len(pricelist)):
        if (pricelist[i] > maxVal): 
            maxVal = pricelist[i]
            maxIndex = i
            
    minVal = maxVal
    
    for j in range(maxIndex, len(pricelist)):
        if (pricelist[j] < minVal):
            minVal = pricelist[j]
    return max(maxVal - minVal, maxLoss(pricelist[0:maxIndex]))

class TestMaxLoss(unittest.TestCase):   
    def test_maxLoss(self):
        self.assertEquals(maxLoss([1,2,3,4,5]), 0) #Ascending list
        self.assertEquals(maxLoss([5,4,3,2,1]), 4) #Descending list
        self.assertEquals(maxLoss([]), 0) #Empty list
        self.assertEquals(maxLoss([aBigList]), 86) #Big list
        self.assertEquals(maxLoss(10,10,10,10,10), 0) #List of identical values