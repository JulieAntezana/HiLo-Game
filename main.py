"""
Project:        HiLo Game
Collaborators:  Julie Antezana, 
                Marcus Ojo- Osasere,
                Lukas Nakale
                Rune Larsen.
Date:           1/20-2022
Last Update:    1/27-2022
"""


from deck import deck
from art import logo
import os

class Hilo:
    """The Hilo class handles the game play, it initializes with the users score and the deck class """

    def __init__(self):
        self.score = 300
        self.deck = deck()
        self.deck.number()
        self.is_playing = True

    def display(self):
        """The display module prints the current card to the user. it takes the first item and
            in the array declared in the deck class"""
        self.current_number = self.deck.numbers[0]
        print(f"The card is: {self.current_number}")

    def user_input(self):
        """The user_input module is loop, asks the user's input, verifies the input then proceeds to call the
            other modules required in the gameplay"""
        while self.is_playing:
            letters = ["l", "h", "q"]
            self.display()
            self.user = input("Higher or lower? (h/l or q for quit): ").lower()

            while self.user not in letters:
                print("Please enter h, l or q")
                self.user = input(
                    "Higher or lower? (h/l or q for quit): ").lower()
            if self.user == "q":
                print(f"Thanks for playing, Your score is: {self.score}")
                self.is_playing = False
                print()
                return

            self.second_number()
            self.compare()

    def second_number(self):
        """The second_number module calls the number module in the deck class which adds a new number to the list of
            The new number is now index 1 and takend as the next number then displayed to the user"""
        self.deck.number()
        self.next_number = self.deck.numbers[1]
        print(f"Next card is: {self.next_number}")

    def compare(self):
        """The compare module compares the user input with the numbers and then computes the score.
            The first number in the numbers list us popped and a check is made to see if the game should continue"""

        if self.user == "h":
            if self.current_number < self.next_number:
                self.score += 100
            else:
                self.score -= 75

        else:
            if self.current_number > self.next_number:
                self.score += 100
            else:
                self.score -= 75

        self.deck.numbers.pop(0)
        print(f"Your score is: {self.score}")
        print()
        if self.score <= 0:
            self.is_playing = False
            self.play_again = input("Game Over. Play again? (y/n): ")
            if self.play_again == "y" or self.play_again == "Y":
                main()


def main():
    hilo = Hilo()
    os.system('cls||clear')
    print(logo)
    hilo.user_input()


if __name__ == "__main__":
    main()

