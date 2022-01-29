import random


class deck:
    """The deck class initializes with an array to store the numbers used in the game class

    number module generates a random number from the range of 1 and 13 then it adds it to the numbers listed
    if the generated number is already in the list, it would generate a new one

    """

    def __init__(self):
        self.drawcard = []

    def current(self):
        """Generates a random number from the range of 1 and 13 then it adds it to the drawcard listed
            if the generated number is already in the list, it would generate a new one"""
        self.current_number = random.randint(1, 13)
        while self.current_number in self.drawcard:
            self.current_number = random.randint(1, 13)
        self.drawcard.append(self.current_number)

    def hidden(self):
        """The hidden module calls the number module in the deck class which adds a new number to the list of
            The new number is now index 1 and taken as the next number then displayed to the user"""
        self.current()
        self.next_number = self.drawcard[1]
        print(f"Next card is: {self.next_number}")

    def high(self):
        if self.hidden > self.current:
            return

    def shuffle(self):
        self.drawcard.pop(0)
