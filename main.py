import numpy as np

def genMultiplications(N) : 
    numbers = set([1])
    for i in range(N) : 
       # The nested loop over j here is run for every i value.  Calculations
       # are thus done for i=0, j=0, then i=0, j=1, then i=1, j=0 and finally i=1, j=1.
       for j in range(i+1) :
          numbers.add(i*j)
    return numbers
    
for i in range(1,10): print( genMultiplications(i) )
