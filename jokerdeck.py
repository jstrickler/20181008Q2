#!/usr/bin/env python

from carddeck import CardDeck

class InventoryItem():
    pass

class JokerDeck(CardDeck):

    def _create_deck(self):
        super()._create_deck()
        self._cards.append(('Joker', ''))
        self._cards.append(('Joker', ''))


