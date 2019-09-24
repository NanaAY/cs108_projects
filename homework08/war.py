'''A Python program that simulates a simplified version of the card game War.
Created Spring 2018
Homework08
@author: Nana Osei Asiedu Yirenkyi (na29)'''


import sys #Imports the system-specific parameters and functions 
import random 


#Create a class that models a standard playing card
class Card():
    '''Models standard playing cards
    Invariable: 
    Suit has to be one of "S", "D", "H", "C"
    and number has to be a value between 1 and 13 inclusive'''
    
    def __init__(self, suit= 'S', number= 9):
        
    
        if (suit in 'SDHC') and (1 <= number <= 13): #ensuring invariants are satisfied
            self._suit = suit
            self._number = number
            
        else:
            print('Wrong Suit or Number', file=sys.stderr)
            sys.exit(-1)
            
        
        
    def get_number(self):
        '''Accesses and returns number'''
        
        return self._number
    
    
    def get_suit(self):
        '''Accesses and returns suit'''
        
        return self._suit
    
    
    def __str__(self):
        '''Returns Cards in appropriate string format'''
        
        if self._number == 1: #converts card with number 1 to an ace
            self._number = 'A'
            
        elif self._number == 11: #converts card with number 11 to a Jack
            self._number = 'J'
            
        elif self._number == 12: #converts card with number 12 to a Queen
            self._number = 'Q'
            
        elif self._number == 13: #converts card with number 13 to a King
            self._number = 'K'
        
        return str(self._number) + self._suit #Return number and first letter of suit
    
    
    def __lt__(self, other):
        '''Compares two cards and returns True if the first is less than the second'''
        
        if self.get_number() == 'A': #gives Ace a value of 14
            self._number = 14
        
        elif other.get_number() == 'A': #gives Ace a value of 14
            other._number = 14
            
        elif self.get_number() == 'K': #gives King a value of 13
            self._number = 13
        
        elif other.get_number() == 'K':  #gives King a value of 13
            other._number = 13
            
        elif self.get_number() == 'Q':  #gives Queen a value of 12
            self._number = 12
        
        elif other.get_number() == 'Q': #gives Queen a value of 12
            other._number = 12
            
        elif self.get_number() == 'J': #gives Jack a value of 11
            self._number = 11
        
        elif other.get_number() == 'J': #gives Jack a value of 11
            other._number = 11
        
            
        return self.get_number() < other.get_number()
    
    
    def __eq__(self, other):
        '''Compares two cards and returns True if they are equal '''
        
        if self.get_number() == 'A':  #gives Ace a value of 14
            self._number = 14
        
        elif other.get_number() == 'A':  #gives Ace a value of 14
            other._number = 14
            
        elif self.get_number() == 'K': #gives King a value of 13
            self._number = 13
        
        elif other.get_number() == 'K': #gives King a value of 13
            other._number = 13
            
        elif self.get_number() == 'Q': #gives Queen a value of 12
            self._number = 12
        
        elif other.get_number() == 'Q': #gives Queen a value of 12
            other._number = 12
            
        elif self.get_number() == 'J': #gives Jack a value of 11
            self._number = 11
        
        elif other.get_number() == 'J': #gives Jack a value of 11
            other._number = 11
        
        return self.get_number() == other.get_number()
    
    
    def __gt__(self, other):
        '''Compares two cards and returns True if the first is greater than the second'''
        
        if self.get_number() == 'A': #gives Ace a value of 14
            self._number = 14
        
        elif other.get_number() == 'A': #gives Ace a value of 14
            other._number = 14
            
        elif self.get_number() == 'K': #gives King a value of 13
            self._number = 13
        
        elif other.get_number() == 'K': #gives King a value of 13
            other._number = 13
            
        elif self.get_number() == 'Q': #gives Queen a value of 12
            self._number = 12
        
        elif other.get_number() == 'Q': #gives Queen a value of 12
            other._number = 12
            
        elif self.get_number() == 'J': #gives Jack a value of 11
            self._number = 11
        
        elif other.get_number() == 'J': #gives Jack a value of 11
            other._number = 11
            
        
        return self.get_number() > other.get_number()
    
       
        
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TESTS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
if __name__ == '__main__':
    
    print('Testing Card class....')    
               
    card1 = Card('S', 8) #Construct a card object with the values.
    print('card1:', card1)    #Print the object.   
    
    card2 = Card('D', 1) #Construct a card object with the values.
    print('card2:', card2,) #Print the object.
    
    card3 = Card('H', 12) #Construct a card object with the values.
    print('card3:', card3) #Print the object.
    
    card4 = Card('C', 11) #Construct a card object with the values.
    print('card4:', card4) #Print the object.
    
    card5 = Card('S', 13) #Construct a card object with the values.
    print('card5:', card5) #Print the object.
    
    card6 = Card('H', 7) #Construct a card object with the values.
    print('card6:', card6) #Print the object.
    
    print('\nTesting Card comparison....')   
    # Compares The different card objects created
    comparison1 = card1 == card2
    print('card1 = card2:', comparison1)
    
    comparison2 = card5 == card3
    print('card5 = card3:', comparison2)
    
    comparison3 = card1 > card2
    print('card1 > card2:', comparison3)
    
    comparison4 = card2 > card5
    print('card2 > card5:', comparison4)
    
    comparison5 = card3 < card5
    print('card3 < card5:', comparison5)
    
    comparison6 = card1 < card2
    print('card1 < card2:', comparison6)
    
    comparison7 = card1 < card1
    print('card1 < card1:', comparison7)
    
    comparison8 = card5 == card5
    print('card5 = card5:', comparison8)
    
    comparison9 = card3 > card3
    print('card3 > card3:', comparison9)
            
            
            
                            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MAIN CODE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
print('\n            STARTING.....')
#creates two empty list of cards for both players
hand1 = [] 
hand2 = []

# Creates a list of possible Suits
suits = ['S','D','H','C'] 

#adds random cards to the two lists of cards
for i in range(5):
    hand1.append(str(Card(random.choice(suits), random.randint(1, 13))))
    hand2.append(str(Card(random.choice(suits), random.randint(1, 13))))
   
#Prints the two lists of cards    
print('\nHand1:', hand1)
print('Hand2:', hand2)

#Keeps track of player scores
player1_score = 0
player2_score = 0

#Compares cards in the two lists
for card1 in range(len(hand1)):
        if hand1[card1] > hand2[card1]:
            player1_score += 1
        elif hand1[card1] < hand2[card1]:
            player2_score += 1
        
            
#Determines and prints the winner            
if player1_score > player2_score:
    print('\nPlayer 1:', player1_score,'\nPlayer 2:', player2_score,'\nPlayer 1 won the game!')
    
elif player1_score < player2_score:
    print('\nPlayer 1:',player1_score,'\nPlayer 2:', player2_score,'\nPlayer 2 won the game!')
    
else:
    print('\nTie! No one wins!\nPlayer 1:',player1_score,'\nPlayer 2:', player2_score)
    
    





