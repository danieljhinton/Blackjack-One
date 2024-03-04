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

# Testing deck class

card_shoe = Deck(8)
card_shoe.shuffle()
print(len(card_shoe.all_cards))


# Player class

class Player:
    
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return f'Balance: ${self.balance:,}'


# Functions which prompt player for game settings when starting a new game

def starting_balance():

    while True:

        try:
            balance = int(input('Enter starting balance (100 - 1,000,000): '))
        except:
            print('Please enter a number between 100 and 1,000,000')

        if 100 <= balance <= 1000000:
            return balance
        else:
            print('Please enter a number between 100 and 1,000,000')


def number_of_decks():
    
    while True:

        try:
            num_of_decks = int(input('Enter number of decks (1-8): '))
        except:
            print('Please enter a number betwen 1 and 8')
    
        if 1 <= num_of_decks <= 8:
            return num_of_decks
        else:
            print('Please enter a number betwen 1 and 8')


# Game logic

card_shoe = Deck(number_of_decks())
player_one = Player(starting_balance())