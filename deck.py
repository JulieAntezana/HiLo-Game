import random

class deck:
    """The deck class initializes with an array to store the numbers used in the game class

    number module generates a random number from the range of 1 and 13 then it adds it to the numbers listed
    if the generated number is already in the list, it would generate a new one

    """

    def __init__(self):
        self.numbers = []

    def number(self):
        """Generates a random number from the range of 1 and 13 then it adds it to the numbers listed
            if the generated number is already in the list, it would generate a new one"""
        self.current_number = random.randint(1, 13)
        while self.current_number in self.numbers:
            self.current_number = random.randint(1, 13)
        self.numbers.append(self.current_number)