try:
    from AssCheck import funcchecks as fc
except:

    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AssCheck"])
    from AssCheck import funcchecks as fc

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_vals_correct(self) :
        inputs, outputs = [],[]
        for i in range(2,10) : 
            inputs.append((i,))
            myset = set([0])
            for j in range(i) : 
                for k in range(j+1) : myset.add(j*k)
            outputs.append( myset )
        assert( fc.check_func( 'genMultiplications', inputs, outputs ) )
