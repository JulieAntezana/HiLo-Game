import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


class Card:
    # A code template for the category of things known as Card. The
    # responsibility of a card is to display a random choice from the
    # array of numbers 1 - 13.

    def __init__(self):
        # A special method, called a constructor, that initializes two
        # attributes. It is invoked using the class name followed by parentheses.

        self.random_card = random.choice(deck)

    def show_card(self):
        # A method that displays the value of the random.choice number.

        print(f"The card is: {self.random_card}")


def main():
    card = Card()
    card.random_card
    card.show_card()


if __name__ == "__main__":
    main()
