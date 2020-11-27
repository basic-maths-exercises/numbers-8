import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_repeated_values(self) :
        for i in range(2,10) : 
            vals = genMultiplications(i)
            for j in range(1,len(vals) ) : 
                for k in range(j) :
                    self.assertFalse( vals[j]==vals[k], "Found multiple values that are the same in the output" )
                    
    def test_vals_correct(self) :
        for i in range(2,10) : 
            vals = genMultiplications(i)
            for j in range(i) : 
               for k in range(j) : 
                   vv = j*k
                   found=False
                   for d in vals : 
                       if d==vv : found=True
                   self.assertTrue( found, "The values in your array are not correct" )
