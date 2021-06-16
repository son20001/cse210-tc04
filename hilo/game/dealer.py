import random

class Dealer:
    EMPTY = False

    def __init__(self):
        self.card = []
        self.choose = ""

    def draw_cards(self):
        if len(self.card) == 0:
            self.card.append(random.randint(1,13))
            self.card.append(random.randint(1,13))
        else:
            self.card.append(random.randint(1,13))


    def ask_guess(self):
        while True:
            self.choose = input("Higher or lower? [h/l] ")
            if choose == 'h' or choose == 'l':
                break
            else:
                print("Enter only h or l")
    def judge(self):
        result = False
        if (choose == 'h' and card[1] > card[0]) or (choose == 'l' and card[1] < card[0]):
            result = True
        else:
            result = False
        self.card.pop(0)
        return result

    def get_points(self):
        pass