# BLACKJACK GAME
'''
We have a computer dealer and a human player.
We have a deck of 52 cards
The human player also has a bank account which can use to make bets.
The dealer starts with 1 card up and 1 card down.
The player starts with 2 cards up.

PLAYER GOAL: get close to a total value of 21 than the dealer does.

POSSIBLE ACTIONS:
    1. Hit (receive another card);
    2. Stay (stop receiving cards);

AFTER PLAYER TURN:
If player is under 21, dealer then hits until they either beat the player or busts.
Computer can win if its sum is higher than player's one AND still under 21

SPECIAL RULES:
Face Cards (Jack, Queen, King) count as a value of 10.
Aces can count on either 1 or 11 whichever is preferable to the player.
'''
# IMPORTING USEFUL LIBRARIES
import random

# -------------------------- FUNCTIONS ------------------------------- #

# CREATE A FUNCTION THAT ASKS HOW MUCH MONEY THE PLAYER HAS
def bank_account():
    while True:
        try:
            amount_of_money = int(input('How much money do you have?  '))
        except ValueError:
            print('You must provide an amount in numbers')
            continue
        else:
            return amount_of_money

# CREATE A FUNCTION THAT GIVES THE FIRST TWO CARDS TO THE PLAYER AND TO THE DEALER
def initial_cards(player_list, dealer_list):
    deck = Deck()
    for i in range(0,2):
        player_list.append(deck.choose_card())
        dealer_list.append(deck.choose_card())

# FIND TOTAL VALUE OF CARDS LIST
def total_value(player_list, player_list_value):
    deck = Deck()
    # need to reduce the value of player's cards to zero since everytime we call the functon it will sum the old value with the new one
    player_list_value = 0
    for x in range(0,len(player_list)):
        player_list_value += deck.find_card_value(player_list[x])
    return player_list_value

# --------------------------- CLASSES ------------------------------- #

# CREATE THE COMPUTER DEALER CLASS
class Dealer:

    def __init__(self):
        pass

# CREATE THE HUMAN PLAYER CLASS
class Player:

    def __init__(self, balance):
        # inheriting the deck class to use its methods
        Deck.__init__(self)
        self.balance = balance

    def bet(self):
        while True:
            try:
                bet_amount = int(input('\nHow much do you want to bet?\n€'))
                if bet_amount > self.balance:
                    print('\nBet amount can not exceed your balance')
                    continue
            except ValueError:
                print('\nYou must provide an amount in numbers')
                continue
            else:
                return bet_amount

    def lose_bet(self,bet):
        print('\nDEALER WINS!!!')
        self.balance -= bet
        print(f'\nYour balance now is:\t{self.balance}')

    def win_bet(self,bet):
        print('\nPLAYER WINS!!')
        self.balance += bet
        print(f'\nYour balance now is:\t{self.balance}')

    # METHOD THAT ASKS THE PLAYER IF HE WANTS A NEW CARD OR IF HE IS DONE
    def move(self):
        while True:
            player_move = input('\nWhat do you want to do now? (\'Hit\' get another card, \'Stay\' stop with the cards you have)\n')
            if player_move.upper() == 'HIT':
                return True
            elif player_move.upper() == 'STAY':
                return False
            else:
                print('Wrong move, please just answer with \'Hit\' or \'Stay\'')
                continue
# CREATE THE DECK CLASS
class Deck:

    cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

    values = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

    def __init__(self):
        pass

    # CHOOSE A RANDOM CARD FROM THE DECK
    def choose_card(self):
        return random.choice(self.cards)

    # FIND ITS VALUE, IF IT'S ACE ASK IF IT MUST BE 1 OR 11
    def find_card_value(self,card):
        # IF IT'S ACE ASK IF THE VALUE MUST BE 1 OR 11
        if card == 'Ace':
            while True:
                try:
                    value_of_ace = int(input('Which value do you want to give to the Ace (1 or 11)?\n'))
                except:
                    print('You must provide a number!')
                else:
                    if (value_of_ace == 1 or value_of_ace == 11):
                        self.values[card] = value_of_ace
                        print(f'Perfect the value of the card is {value_of_ace}')
                        return self.values[card]
                    else:
                        print('You must provide a correct number (1 or 11)')
                        continue
        # IF IT'S A NORMAL CARD JUST RETURN THE VALUE OF THE CARD
        else:
            return self.values[card]

# ---------------------------- GAME SETUP ----------------------------- #
print('Welcome in our Casinò get ready to play!!')
# DEFINE THE DECK CLASS AND SAVE IT INTO A VARIABLE
deck = Deck()
# ASK THE PLAYER HOW MUCH MONEY DOES HE HAVE AND SAVE SUCH AMOUNT INTO A VARIABLE
balance = bank_account()
# DEFINE THE PLAYER VARIABLE AND USE THE BALANCE YOU PREVIOUSLY SAVED
player = Player(balance)
print(f'Perfect! Your balance is €{player.balance}\n')

# CREATE A LOOP THAT WILL STOP WHEN THE BALANCE OF THE USER WILL BECOME 0
while player.balance > 0:
    # INSIDE THE LOOP CREATE A LIST FOR THE CARDS OF THE PLAYER AND ANOTHER LIST FOR THE CARDS OF THE DEALER
    player_cards = []
    dealer_cards = []
    value_of_player_cards = 0
    value_of_dealer_cards = 0
    print('Mixing cards...\n\n')
    # USE A FUNCTION THAT CHOOSES FOUR RANDOM CARDS AND ASSIGN THEM TO THE PLAYER CARDS LIST AND DEALER CARDS LIST
    initial_cards(player_cards, dealer_cards)
    # SHOW THE CARDS
    print(f'Your cards are:  {player_cards[0]}  {player_cards[1]}')
    print(f"Dealer's card is:  {dealer_cards[0]}")
    # USE A FUNCTION TO EVALUATE THE TOTAL VALUE OF THE CARDS OF THE PLAYER AND THE DEALER
    value_of_player_cards = total_value(player_cards, value_of_player_cards)
    value_of_dealer_cards = total_value(dealer_cards, value_of_dealer_cards)

    bet = player.bet()
    # PLAYER TURN
    # UNITL THE PLAYER DOESNT BUST KEEP ASKING HIM WHAT'S HIS MOVE
    while value_of_player_cards <= 21:
        player_move = player.move()
        # IF HE HITS ON A NEW CARD
        if player_move:
            player_cards.append(deck.choose_card())
            print('\nYour cards are:')
            for x in player_cards:
                print(f'{x}')
            value_of_player_cards = total_value(player_cards, value_of_player_cards)
        # ELSE IF HE IS FINE WITH HIS CARDS
        else:
            print('\nThank you! Now it\'s Dealer\'s turn')
            break
        # IN CASE THE PLAYER BUSTS RESTART THE MATCH
    else:
        print('\nSorry you went too far!!')
        player.lose_bet(bet)
        continue

    # DEALER TURN
    # WHILE DEALER' SCORE IS LOWER THAN PLAYER' SCORE KEEP HITTIG ON NEW CARDS
    while value_of_dealer_cards < value_of_player_cards:
        dealer_cards.append(deck.choose_card())
        value_of_dealer_cards = total_value(dealer_cards, value_of_dealer_cards)
        # IF DEALER EXCEEDS 21 HE LOSES
        if value_of_dealer_cards > 21:
            print('\nDealer\'s cards are:\n')
            for x in dealer_cards:
                print(f'{x}')
            print('\nDealer busted.')
            player.win_bet(bet)
            break
    else:
        player.lose_bet(bet)
else:
    print('GAME OVER! You finished your money!')
