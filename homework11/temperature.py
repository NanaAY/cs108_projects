'''This python program is a models for a temperature conversion program 
Created Spring 2018
Homework11
@author Nana Osei Asiedu Yirenkyi(na29) '''


class Temperature:
    '''Temperature converter.
    Invariants: No temperature should be below absolute zero. '''
    def __init__(self,temp=0.0):
        ''''''
        if temp > -459.67:
            self._temp = float(temp)
        else:
            raise ValueError('Temperature should not be below absolute zero(–459.67°F.)')
    
    def get_temp(self):
        '''Accesses and returns the default temperature in fahrenheit'''
        return self._temp
    
    def get_temp_celsius(self,temp_in_fahreinheit):
        '''Accesses and returns the temperature in celsius'''
        self._temp = float(temp_in_fahreinheit)
        celsius = (self._temp - 32) / 1.8
        return celsius
    
if __name__ == '__main__':
    # Do a simple test 
    temp = Temperature()
    print(temp.get_temp())
    print(temp.get_temp_celsius(-5))
