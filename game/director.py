from game.card import Card


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (List[Card]): A list of card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.card = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if the next card will be higher or lower.

        Args:
            self (Director): An instance of Director.
        """
        card = Card()
        card.random_card
        card.show_card()

        guess_card = input("Higher or lower? [h/l] ")
        self.is_playing = (guess_card == "")
        if (guess_card == "H" or guess_card == "h"):
            guess_card == "higher"

        elif (guess_card == "L" or guess_card == "l"):
            guess_card == "lower"

        print(guess_card)

        card = Card()
        card.random_card
        card.show_card()

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points

            self.total_score += self.score
            self.score = 0

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "

        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        # self.is_playing == (self.score > 0)
        if self.score == 0
        self.is_playing = False
