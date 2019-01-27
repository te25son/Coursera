from random import shuffle
import time

SUITES = "H D S C".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
TABLE_CARDS = []


class Deck:

    def __init__(self):
        self.deck = [(e,f) for e in SUITES for f in RANKS]

    def shuffle(self):
        shuffle(self.deck)

    def split(self):
        self.deck1 = [e for e in self.deck if self.deck.index(e) % 2 == 0]
        self.deck2 = [e for e in self.deck if self.deck.index(e) % 2 != 0]
        return (self.deck1, self.deck2)

class Hand:

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        print("Contains {} cards".format(len(self.cards)))

    def add(self, cards):
        self.cards.extend(cards)

    def remove(self):
        return self.cards.pop()

class Player:

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove()
        print("{} has placed {}".format(self.name, drawn_card))
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            # return self.hand.cards[:-1]  # return all cards up to but not including the last one
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove())
            return war_cards

    def still_has_cards(self):
        """
        Returns True is player still has cards
        """
        return len(self.hand.cards) != 0


# def check_war(card1, card2):
#     if card1[1] == card2[1]:
#         WAR_COUNT += 1
#         print("!! WAR !!")
#         play_war(card1, card2)
#
# def play_war(card1, card2):
#     TABLE_CARDS = []
#     TABLE_CARDS.extend(user.remove_war_cards())
#     TABLE_CARDS.extend(comp.remove_war_cards())







print("Welcome to war, let's begin...")

# create new deck and split in half
d = Deck()
d.shuffle()
half1, half2 = d.split()

# create new players
# set computer player
comp = Player("Computer", Hand(half1))
# get user name
name = input("What's your name? ")
# set user player
user = Player(name, Hand(half2))

TOTAL_ROUNDS = 0
WAR_COUNT = 0

while user.still_has_cards() and comp.still_has_cards():
    TOTAL_ROUNDS += 1
    # time.sleep(2)
    print("\n")
    print("Round {}".format(TOTAL_ROUNDS))
    print("+" * 9)
    print("Standings:")
    print("{} has {} cards".format(user.name, str(len(user.hand.cards))))
    print("{} has {} cards".format(comp.name, str(len(comp.hand.cards))))
    print("Play!")
    print("\n")
    # time.sleep(2)

    TABLE_CARDS = []

    p_card = user.play_card()
    c_card = comp.play_card()

    TABLE_CARDS.append(p_card)
    TABLE_CARDS.append(c_card)

    # check if war
    if c_card[1] == p_card[1]:
        WAR_COUNT += 1
        print("WAR!!")
        TABLE_CARDS.extend(user.remove_war_cards())
        TABLE_CARDS.extend(comp.remove_war_cards())

        p_card = user.play_card()
        c_card = comp.play_card()

        TABLE_CARDS.append(p_card)
        TABLE_CARDS.append(c_card)

        print(TABLE_CARDS)

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print("{} wins!".format(user.name))
            user.hand.add(TABLE_CARDS)
        else:
            print("{} wins!".format(comp.name))
            comp.hand.add(TABLE_CARDS)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print("{} wins!".format(user.name))
            user.hand.add(TABLE_CARDS)
        else:
            print("{} wins!".format(comp.name))
            comp.hand.add(TABLE_CARDS)

print("\n")
print("GAME OVER")
print("\n")
print("Number of rounds: {}".format(str(TOTAL_ROUNDS)))
print("Number of wars: {}".format(str(WAR_COUNT)))
