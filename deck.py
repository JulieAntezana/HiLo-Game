import random

class deck:
    
    def __init__(self):
        self.numbers = []
        
    def number(self):
        self.current_number = random.randint(range(1,14))
        while self.current_number in self.numbers:
            self.current_number = random.randint(range(1,14))
        self.numbers.append(self.current_number)
        
        

        
class hilo:
    def __init__(self):
        self.score = 300
        self.deck = deck()
        self.deck.number()
        
        
    def display(self):
        self.current_number = self.deck.numbers[0]
        print(f"The card is: {self.current_number}")
        
    def user_input(self):
        self.next_number()
        self.user = input("").lower()
        pass
    
    def next_number(self):
        self.deck.number()
        self.next_number = self.deck.numbers[1]
        print(f"Next card is: {self.next_number}")
    
    def compare(self):
        if self.user == "h":
            if self.current_number < self.next_number:
                self.score += 100
            else:
                self.score -+ 100
                
        else:
            if self.current_number > self.next_number:
                self.score += 100
            else:
                self.score -+ 100
        
        self.deck.numbers.pop(0)
        print(self.score)
        
    
        
        
        
        
        
        
        

  
"""
class Deck:
    init
    funtion: return a random number from range of 1 and 13
    
Class hilo:
init 
display function:
takes a card from the deck class and then prints its
it asks user input

compare funtion:
new number from the deck class 


"""        