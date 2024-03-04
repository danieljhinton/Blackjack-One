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
            balance = int(input('\nEnter starting balance (100 - 1,000,000): '))
        except:
            print('\nPlease enter a number between 100 and 1,000,000')

        if 100 <= balance <= 1000000:
            return balance
        else:
            print('\nPlease enter a number between 100 and 1,000,000')

def number_of_decks():
    '''
    Get input from user as to how many decks they wish to play with
    '''
    while True:

        try:
            num_of_decks = int(input('\nEnter number of decks (1-8): '))
        except:
            print('\nPlease enter a number betwen 1 and 8')
    
        if 1 <= num_of_decks <= 8:
            return num_of_decks
        else:
            print('\nPlease enter a number betwen 1 and 8')


# Gameplay functions

def player_wager_amount(player):
    '''
    Get input from user as to how much they wish to wager in the next hand,
    from minimum $10 to their full balance, in units of $10
    '''
    while True:

        try:
            wager = int(input('\nEnter bet amount (minimum $10, units $10): '))
        except:
            print(f'\nPlease enter an amount between $10 and ${player.balance}')

        if 10 <= wager <= player.balance and wager % 10 == 0:
            return wager
        else:
            print(f'\nPlease enter an amount between $10 and ${player.balance} in\
 units of $10')

def display_cards(cards):
    '''
    Print a player or dealer's current hand.
    '''
    for i in cards:
        print(i, end = ' ')

def calculate_hand_total(hand):
    '''
    Return the value of the player or dealer's hand (ie. J5 = 15)
    '''
    card_value_list = [i.value for i in hand]
    hand_total = sum(card_value_list)

    if 11 in card_value_list and hand_total > 21:    # Dealing with Aces
        hand_total -= 10

    return hand_total        

def player_option():
    '''
    Take input from user to hit or stay
    '''
    while True:
        decision = input('\n\nHit or Stay? Type H to hit or S to stay: ').strip()\
            .lower()
        if decision in ('h', 's'):
            return decision
        else:
            print('Invalid input.')


def betting_round(wager):
    '''
    Betting round logic. Takes wager amount as input, returns winnings.
    '''
    global player_one, card_shoe
    dealers_cards = [card_shoe.deal_a_card()]
    players_cards = [card_shoe.deal_a_card(), card_shoe.deal_a_card()]

    dealer_total = calculate_hand_total(dealers_cards)
    player_total = calculate_hand_total(players_cards)

    print('\nDealer: ', end = '')
    display_cards(dealers_cards)

    print('\n\nPlayer: ', end = '')
    display_cards(players_cards)

    if player_total == 21:    # Resolving the hand if player has blackjack
        if dealer_total in (10, 11):
            print('Blackjack!\nChecking for dealer Blackjack: ')
            dealers_cards.append(card_shoe.deal_a_card())
            display_cards(dealers_cards)
            dealer_total = calculate_hand_total(dealers_cards)
            if dealer_total == 21:
                print('Blackjack! Stand off!')
            else:
                print(f'Winner! You won {wager * 1.5:,}!')
                return wager * 1.5
    else:
        while player_total < 21:
            player_decision = player_option()
            if player_decision == 'h':
                players_cards.append(card_shoe.deal_a_card())
                player_total = calculate_hand_total(players_cards)
                print('\nPlayer: ', end = '')
                display_cards(players_cards)
            else:
                break

    if player_total > 21:    # Ending the hand if the player busted
        print('\nBust!')
        return 0
    
    while dealer_total < 17:    # Dealing the dealer's cards
            dealers_cards.append(card_shoe.deal_a_card())
            dealer_total = calculate_hand_total(dealers_cards)
            print('\nDealer: ', end = '')
            display_cards(dealers_cards)

    if dealer_total > 21:    # Resolving the hand if the dealer busted
        print(f'\nDealer busted! Winner! You won ${wager * 2:,}')
        return wager * 2

    if player_total > dealer_total:
        print(f'\n\nWinner! You won ${wager * 2:,}')
        return wager * 2
    elif player_total == dealer_total:
        print('\n\nStand-off!')
        return wager
    else:
        print('\n\nYou lost.')
        return 0

# Game logic

card_shoe = Deck(number_of_decks())
player_one = Player(starting_balance())
card_shoe.shuffle()

game_on = True

while game_on:
    
    print(f'\nCurrent balance: ${player_one.balance:,}')
    wager = player_wager_amount(player_one)
    winnings = betting_round(wager)
    player_one.balance -= wager
    player_one.balance += winnings
