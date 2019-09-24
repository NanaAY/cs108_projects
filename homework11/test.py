'''
Unit test the temperature class
Spring 2018
@author: Nana Osei Asiedu Yirenkyi (na29)
'''

import unittest
from temperature import Temperature


class Test(unittest.TestCase):
    
    def setUp(self):
        ''' 
        Set up the temperature converter for each of the unit tests 
        This function is run once, before each of the test methods below.
        '''
        self.temp = Temperature()
        
        
    def test_temp(self):
        try:
            assert self.temp.get_temp() == 0.0
        except:
            self.fail('This should not raise an exception')
            
        
    def test_conversion(self):
        try:
            assert self.temp.get_temp_celsius() == -17.77777777777778
            assert self.temp.get_temp_celsius(50) == 10
            assert self.temp.get_temp_celsius(-4) == -20
        except:
            self.fail('This should not raise an exception')
            
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()