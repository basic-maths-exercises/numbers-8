import numpy as np

numbers = []
for i in range(2) : 
  # The nested loop over j here is run for every i value.  Calculations
  # are thus done for i=0, j=0, then i=0, j=1, then i=1, j=0 and finally i=1, j=1.
  for j in range(2) : 
    numbers.append(i*j)
    
print( numbers )
