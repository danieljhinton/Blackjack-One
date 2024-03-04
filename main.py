import random


# Card data

suits = ('♠', '♥', '♦', '♣')

ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')

values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10,
          'J':10, 'Q':10, 'K':10, 'A':11}    # Make A 1 or 11


# Card class

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank}{self.suit}'
    

# Deck class - Create a deck of cards with functions to shuffle and deal one.
# Takes single int argument for number of decks (Blackjack can be played with
# 1-8 decks depending on the game rules)

class Deck:

    def __init__(self, num_of_decks):
        self.all_cards = []
        for i in range(num_of_decks):
            for suit in suits:
                for rank in ranks:
                    self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_a_card(self):
        return self.all_cards.pop()

card_shoe = Deck(8)
card_shoe.shuffle()
print(len(card_shoe.all_cards))