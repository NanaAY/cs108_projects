''' A Card Game War Program
Created Fall 2014
Homework 08
@author: Karen CUdjoe (kec32)
'''

#import the system-specific parameters and functions using import sys
import sys

#import random
import random

#Create a class that models a standard playing card
class Cards:
    '''
    Models standard playing cards
    Invariants 
    Numbers should be between 1 and 13 (inclusive)
    Suits must be spade, heart, club or diamond
    Suit must not be joker
    '''
    
    #Add instance variables to a Fraction class
    def __init__(self, number = 1, suit = 'spade'):
        '''
        () = Cards
        Constructor
        '''
        #If the number satisfies the invariant, set self._number to number. 
        if 1 <= number <= 13:
            self._number = number
        #Else print invalid number and exit    
        else:
            print("Invalid number",file=sys.stderr)
            sys.exit(-1)
        #If the suit satisfies the invariant, set self._suit to suit   
        if suit == 'spade' or suit == 'heart' or suit == 'club' or suit == 'diamond':
            self._suit = suit
        #Else print invalid suit and exit
        else:
            print("Invalid suit", file=sys.stderr)
            sys.exit(-1)
            
    #accessors
    def get_number(self):   
        '''accessors for number'''
        return self._number
    
    def get_suit(self):
        '''accessors for suit'''
        return self._suit
    
    #A string method to allow printing of card objects 
    def __str__(self):
        #Return number and first letter of suit
        return (str(self._number)+str(self._suit[0]))
    
    #Overload the comparison operators <, == and > to allow comparison of cards based on suit (An ace is higher than a King)
    #Define the function less than 
    def __lt__(self, other):
        #if your number( self._number) is 1, it is an Ace, and as such it is the highest card. It can't be less than any other card so return False
        if self._number == 1: 
            return False
        #if the other card has the number 1, it is the highest so your card can't be higher than it, so return true
        if other.get_number == 1:
            return True
        #if your number is less than the other number, return True
        if self._number < other.get_number():
            return True
        #else, return false
        else:
            return False
    
    #Define the greater than function   
    def __gt__(self, other): 
        #if the other card has the number 1, it is the highest so your card can't be higher than it, so return False
        if other.get_number == 1:
            return False   
        #if your card has the number 1, it is the highest so the other card can't be higher than it, so return true
        if self._number == 1: 
            return True
        #if your card has the number 1, it is the highest so the other card can't be higher than it, so return true
        if self._number > other.get_number():
            return True
        #else return false
        else:
            return False
    
    #define the equal to function
    def __eq__(self, other):
        #if booth numbers are equal, return true
        if other.get_number == self._number:
            return True
        #else, return false
        else:
            return False
        
        
'''Main code'''
#CReate two empty lists
list1 = []
list2 = []   
#Create a for loop 
for i in range(0, 5):  
    #Append 5 random numbers each to both lists 
    list1.append(Cards(random.randint(1, 13), 'spade'))
    list2.append(Cards(random.randint(1, 13), 'spade' ))

#FOr each element in list one, print it out 
for i in list1:   
    print(i, end=' ')
print()
#FOr each element in list two, print it out
for i in list2:    
    print(i, end = ' ')
 
#Set both counts to 0
count1 = 0
count2 = 0    
#Create a for loop 
#For i in the range of the first list
for i in range(0, len(list1)):
    #if any element i in list one, is greater than any element i in list 2, increase the count of list 1 by 1
    if list1[i] > list2[i]:
        count1 += 1
    #elif, any element i in list two, is greater than any element i in list 1, increase the count of list 2 by 1
    elif list1[i] < list2[i]:
        count2 += 1



print()        
print('player 1 -', count1)
print('player 2 -', count2)


print()        

#if count of list 1 is greater than the count of list two, print player one wins
if count1 > count2:
    print("Player 1 wins")

#elif count of list one is less than count of list two, player two wins   
elif count1 < count2:
    print("Player 2 wins")

#else, if there is a draw, no one wins    
else:
    print("No winner")