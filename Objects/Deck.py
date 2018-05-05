# A module to define the decks of cards being used

from random import sample

class Deck:

    def __init__(self, object_list, object_type):
        self._Deck = object_list
        self._Deck = sample(self._Deck, len(self._Deck))
        self._Count = len(self._Deck)
        self._object_type = object_type

    def return_count(self):
        return self._Count

    def return_deck(self):
        return self._Deck

    def return_card_in_deck(self, index):
        return self._Deck[index]

    def shuffle_deck(self):
        self._Deck = sample(self._Deck, self._Count)

    def put_card_on_top(self, card):
        self._Deck.insert(0, card)
        # puts a card on top of the deck
        pass

    def put_card_on_bottom(self, card):
        self._Deck.append(card)
        # puts a card on the bottom of the deck
        pass

    d

