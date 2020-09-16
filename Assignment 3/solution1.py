from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
values = ('Jack', 'Queen', 'King', 'Ace')


class CardGame():

    def __init__(self):
        # Creates a list of 52 cards a card being a tuple with value(2-14) and (0-4) for suites
        self.deck = []
        for suit_index in range(4):
            for value_index in range(2, 15):
                self.deck.append((value_index, suit_index))

    def card_name(self, card):
        # return a string "Ace of cards" from card being passed in as a tuple
        if card[0] > 10:
            nr = card[0] - 11
            name = str(values[nr])
        else:
            name = card[0]
        suit = suits[card[1]]
        return f'{name} of {suit} '

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
