import random

class Dealer:
    """A code template for a person who throws dice. The responsibility of this 
    class of objects is to throw the dice, keep track of the values, the score 
    and determine whether or not it can throw again.
    
    Attributes:
        DECK (list): all possible numbers that dealer can draw
        card (list): 2 cards that dealer drawed
        choose (string): choose from user as h--higher-- or l--lower--
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Dealer): An instance of Dealer.
        """
        self.DECK = []
        for card in range(1, 14):
            self.DECK.append(card) # [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.card = []
        self.choose = ""

    def draw_cards(self):
        """draw 2 cards from deck

        Args: 
            self (Dealer): An instance of Dealer.
        """
        if len(self.card) == 2: # after first draw in the game
            self.DECK.append(self.card.pop(0))
            self.card.append(self.DECK.pop(random.randrange(0, len(self.DECK))))
        else: # first draw in the game
            self.card.append(self.DECK.pop(random.randrange(0, len(self.DECK))))
            self.card.append(self.DECK.pop(random.randrange(0, len(self.DECK))))

    def ask_guess(self):
        """get input from player, higher or lower

        Args: 
            self (Dealer): An instance of Dealer.
        """
        self.choose = ""
        while True:
            self.choose = input("Higher or lower? [h/l] ")
            if self.choose == 'h' or self.choose == 'l':
                break
            else:
                print("Enter only h or l")
    def judge(self):
        """Determines whether or not player wins or not

        Args: 
            self (Dealer): An instance of Dealer.

        Return:
            True when player win, False when player lose
        """
        if (self.choose == 'h' and self.card[1] > self.card[0]) or (self.choose == 'l' and self.card[1] < self.card[0]):
            return True
        else:
            return False