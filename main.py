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


# Player class

class Player:
    
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return f'Balance: ${self.balance:,}'


# Functions which prompt player for game settings when starting a new game

def starting_balance():
    '''
    Get input from the user as to how much money they wish to start with
    '''
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
    '''
    Get input from user as to how many decks they wish to play with
    '''
    while True:

        try:
            num_of_decks = int(input('Enter number of decks (1-8): '))
        except:
            print('Please enter a number betwen 1 and 8')
    
        if 1 <= num_of_decks <= 8:
            return num_of_decks
        else:
            print('Please enter a number betwen 1 and 8')


# Gameplay functions

def player_wager_amount(player):
    '''
    Get input from user as to how much they wish to wager in the next hand,
    from minimum $25 to their full balance
    '''
    while True:

        try:
            wager = int(input('Enter bet amount (minimum $25): '))
        except:
            print(f'Please enter an amount between $25 and ${player.balance}')

        if 25 <= wager <= player.balance:
            return wager
        else:
            print(f'Please enter an amount between $25 and ${player.balance}')

def display_cards(cards):
    '''
    Print a player or dealer's current hand.
    '''
    for i in cards:
        print(i, end = ' ')

def betting_round(wager):
    '''
    Betting round logic
    '''
    global player_one, card_shoe
    dealers_cards = [card_shoe.deal_a_card()]
    players_cards = [card_shoe.deal_a_card(), card_shoe.deal_a_card()]

    dealer_total = sum([i.value for i in dealers_cards])
    player_total = sum([i.value for i in dealers_cards])

    print('Dealer: ', end = '')
    display_cards(dealers_cards)

    print('\nPlayer: ', end = '')
    display_cards(players_cards)

    if player_total == 21:
        if dealer_total in (10, 11):
            print('Blackjack!\nChecking for dealer Blackjack: ')
            dealers_cards.append(card_shoe.deal_a_card())


# Game logic

card_shoe = Deck(number_of_decks())
player_one = Player(starting_balance())
card_shoe.shuffle()

wager = player_wager_amount(player_one)
betting_round(wager)