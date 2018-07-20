# A module to define the decks of cards being used

from random import sample


class Deck:

    def __init__(self, object_list, object_type):
        self._Deck = sample(object_list, len(object_list))
        self._Object_type = object_type

    def __repr__(self):
        card_list = []
        for i in self._Deck:
            card_list.append(i.name())
        return ', '.join(card_list)

    def return_count(self):
        return len(self._Deck)

    def return_deck(self):
        return self._Deck

    def return_object_type(self):
        return self._Object_type

    def return_card_in_deck(self, index):
        return self._Deck[index]

    def shuffle_deck(self):
        self._Deck = sample(self._Deck, len(self._Deck))

    def put_card_on_top(self, card):
        self._Deck.insert(0, card)
        # puts a card on top of the deck

    def put_card_on_bottom(self, card):
        self._Deck.append(card)
        # puts a card on the bottom of the deck

    def take_card_off_top(self):
        del self._Deck[0]
        # Deletes the top card of the deck

    def take_card_out(self, index):
        del self._Deck[index]
        # Deletes a card of a given index in the deck


