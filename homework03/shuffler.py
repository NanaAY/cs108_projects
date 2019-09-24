'''A python program that thoroughly shuffles a list of values
Created Spring 2018
homework03
@author: Nana Osei Asiedu Yirenkyi(na29)'''

import random


#First create a list containing 26 string

strings = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('list to shuffle:\n', strings)



#ask the user for the number of times list is to be shuffled

numTimes = int(input('\nHow many times should the list be shuffled:'))



#removing random values from the list 'numTimes' times

rand_loc = random.randint(0, len(strings) - 1)

for num in range(numTimes):
    random_letter = strings[rand_loc]
    strings.remove(random_letter)
    strings.append(random_letter)
 
 
 
 
print('\nSHuffled list:\n',strings)   