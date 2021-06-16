from game.dealer import Dealer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:

    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.score = 0
        self.dealer = Dealer()
        self.keep_playing = True

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means throwing the dice.

        Args:
            self (Director): An instance of Director.
            dealer (Dealer): An instance of Dealer.
        """
        self.dealer.draw_cards()
        print(f"The card is: {self.dealer.card[0]}")
        self.dealer.ask_guess()
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        if self.dealer.judge():
            self.score += 100
        else:
            self.score -= 75

            
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the dice that were rolled and the score.

        Args:
            self (Director): An instance of Director.
        """
        print(f"Next card was: {self.dealer.card[1]}")
        print("Your score is: {self.score}")
        if self.score > 0:
            choice = input("Keep playing? [y/n] ")
            self.keep_playing = (choice.lower() == "y")
        else:
            self.keep_playing = False