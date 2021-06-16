import random

class Dealer:
    EMPTY = False

    def __init__(self):
        self.DECK = []
        for card in range(1, 14):
            self.DECK.append(card) # [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.card = []
        self.choose = ""

    def draw_cards(self):
        if len(self.card) == 2: # after first draw in the game
            self.DECK.append(self.card.pop(0))
            self.card.append(self.DECK.pop(random.randrange(0, len(self.DECK))))
        else: # first draw in the game
            self.card.append(self.DECK.pop(random.randrange(0, len(self.DECK))))
            self.card.append(self.DECK.pop(random.randrange(0, len(self.DECK))))

    def ask_guess(self):
        while True:
            self.choose = input("Higher or lower? [h/l] ")
            if self.choose == 'h' or self.choose == 'l':
                break
            else:
                print("Enter only h or l")
    def judge(self):
        if (self.choose == 'h' and self.card[1] > self.card[0]) or (self.choose == 'l' and self.card[1] < self.card[0]):
            return True
        else:
            return False