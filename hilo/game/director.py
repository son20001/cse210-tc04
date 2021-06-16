from game.dealer import Dealer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        dealer (Dealer): An instance of the class of objects known as Dealer.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 0
        self.dealer = Dealer()

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
        that means that dealer drawing cards and that player answer higher or lower.

        Args:
            self (Director): An instance of Director.
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
            if self.score >= 100:
                self.score -= 75
            else:
                self.score = 0


            
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the next card that were drawed and the score.

        Args:
            self (Director): An instance of Director.
        """
        print(f"Next card was: {self.dealer.card[1]}")
        print(f"Your score is: {self.score}")
        if self.score > 0:
            choice = input("Keep playing? [y/n] ")
            self.keep_playing = (choice.lower() == "y")
        else:
            self.keep_playing = False
        print("")