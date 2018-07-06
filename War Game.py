# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print('DECK CREATED')
        self.allCards = [(s,r) for s in SUITE for r in RANKS]

    def deckShuffle(self):
        print('Shuffling Deck')
        shuffle(self.allCards)

    def splitAndReturn(self):
        return (self.allCards[:26], self.allCards[26:])
        

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def addCards(self, addedCards):
        self.cards.extend(addedCards)

    def removeCard(self):
        return self.cards.pop()

class Player(Hand):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def playCard(self):
        drawnCard = self.hand.removeCard()
        print("{} has placed: {}".format(self.name, drawnCard))
        return drawnCard

    def removeWarCard(self):
        warCards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                warCards.append(self.hand.removeCard())
            return warCards

    def stillHasCards(self):
        #Return true if player has card left
        return len(self.hand.cards) != 0

######################
#### GAME PLAY #######
######################
def main():
    print("Welcome to War, let's begin...")

    # Use the 3 classes along with some logic to play a game of war!

    #Create a new deck and split in half
    d = Deck()
    d.deckShuffle()
    half1, half2 = d.splitAndReturn()

    comp = Player("Computer", Hand(half1))

    name = input("What is your name ?")
    user = Player(name, Hand(half2))

    # Start Playing
    total_rounds = 0
    war_count = 0

    # check if both the players still has cards left
    while comp.stillHasCards() and user.stillHasCards():
        total_rounds += 1
        print("Time for a new Round")
        print("Current Standings:")
        print(user.name+" has the count: "+str(len(user.hand.cards)))
        print("Comp has the count: "+str(len(comp.hand.cards)))
        print("Play a card\n")

        tableCard = [] # Used to store the cards on the table

        c_card = comp.playCard()
        u_card = user.playCard()

        tableCard.append(c_card)
        tableCard.append(u_card)

        # Check for War Condition
        if c_card[1] == u_card[1]:
            war_count += 1
            print("War!!")

            tableCard.extend(user.removeWarCard())
            tableCard.extend(comp.removeWarCard())

            #Draw new card
            c_card = comp.playCard()
            u_card = user.playCard()

            # Compare the Ranks of cards
            if RANKS.index(c_card[1]) < RANKS.index(u_card[1]):
                user.hand.addCards(tableCard)
            else:
                comp.hand.addCards(tableCard)
            
        else:
            if RANKS.index(c_card[1]) < RANKS.index(u_card[1]):
                user.hand.addCards(tableCard)
            else:
                comp.hand.addCards(tableCard)

    print("Game Over ! Number of Rounds: "+str(total_rounds))
    print("War happened "+str(war_count)+" times")
    
    if comp.stillHasCards():
        print("Computer has Won!")
    else:
        print(str(user.name)+" has Won!")

if __name__ == "__main__":
    main()

