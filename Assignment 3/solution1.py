"""
Problem 1: (10pt)

Define a CardGame () class allowing you to instantiate objects whose behavior is similar to that of a real card game. The class must include the following methods

constructor method: creation and filling of a list of 52 elements, which are themselves tuples of 2 integers. 
This list of tuples will contain the characteristics of each of the 52 cards. For each of them, 
it is in fact necessary to store separately an integer indicating the value 
(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, the last 4 values ​​being those Jack, Queen, King and Ace), and another integer indicating 
the suit of the card (i.e. 0,1,2,3 for Hearts, Diamonds, Clubs and Spades). In such a list, element (11,2) therefore designates the jack of clubs, 
and the completed list must be of the type: [(2, 0), (3.0), (3.0), (4 , 0), ..... (12.3), (13.3), (14.3)]

card_name () method: this method must return, in the form of a string, the identity of any card for which 
it has been given the descriptor tuple as an argument. For example, the instruction: print game.card_name ((14, 3)) should cause the display of: Ace of spades

shuffling method (): as everyone knows, shuffling the cards consists of shuffling them. 
This method is therefore used to shuffle the elements of the list containing the cards, regardless of the number.

draw () method: when this method is invoked, a card is removed from the game. The tuple containing its value and color is returned to the calling program. 
We always take the first card off the list. If this method is invoked when there are no cards left in the list, 
then the special object None must be returned to the calling program.

Lets play a little game with our cardGame class: define two players A and B. 
Instantiate two sets of cards (one for each player) and shuffle them. 

Then, using a loop, draw a card from each of the two decks 52 times and compare their values. 
If the first of the two has the higher value, we add a point to player A. 
If the opposite situation arises, we add a point to player B. If the two values are equal, we go to the draw. 
At the end of the loop, compare the counts of A and B to determine the winner.

 

Example:

Player A vs Player B:

2 of Clubs * 6 of Clubs ==> Points : 0 * 1

2 of Spades * 3 of Clubs ==> Points : 0 * 2

ace of Diamond * 7 of Clubs ==> Points : 1 * 2

…

king of Hearts * 6 of Diamond ==> Points : 24 * 27

ace of Hearts * 10 of Clubs ==> Points : 25 * 27

Player A has 25 points, Player B has 27.

Winner : Player B
"""
from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
values = ('No card', 'No card', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
          'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class CardGame():

    def __init__(self):
        # Creates a list of 52 cards a card being a tuple with value(2-14) and (0-4) for suites
        self.deck = []
        for suit_index in range(4):
            for value_index in range(2, 15):
                self.deck.append((value_index, suit_index))

    def card_name(self, card):
        # return a string "Ace of cards" from card being passed in as a tuple
        return f'{values[card[0]]} of {suits[card[1]]} '

    def shuffle(self):
        # Shuffle the deck
        shuffle(self.deck)

    def draw(self):
        # removes a card from the game and returns the card being pulled from the deck
        if len(self.deck) > 0:
            return self.deck.pop(0)
        else:
            return None


game_on = True
playerA = CardGame()
playerB = CardGame()
playerA.shuffle()
playerB.shuffle()
playerA_score = 0
playerB_score = 0

print("Player A vs Player B:")

while game_on:
    playerA_card = playerA.draw()
    playerB_card = playerB.draw()
    if playerA_card == None or playerB_card == None:
        game_on = False
        if playerA_score > playerB_score:
            print("Winner: Player A")
        elif playerB_score > playerA_score:
            print("Winner: Player B")
        else:
            print("It's a draw")
    else:
        if playerA_card[0] > playerB_card[0]:
            playerA_score += 1
        elif playerB_card[0] > playerA_card[0]:
            playerB_score += 1
        print(
            f"{playerA.card_name(playerA_card)} ==> {playerB.card_name(playerB_card)}: {playerA_score} * {playerB_score}")
