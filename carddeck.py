#!/usr/bin/env python
import random


class CardDeck():
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):
        self._dealer = dealer
        self._create_deck()


    def _create_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards


    # def get_dealer(self):
    #     return self._dealer
    #
    # def set_dealer(self, dealer):
    #     if isinstance(dealer, str):
    #         self._dealer = dealer
    #     else:
    #         raise TypeError("Dealer must be a string")
    #

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop(0)

    @property
    def dealer(self):
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @classmethod
    def get_suits(cls):
        return cls.SUITS


    def __len__(self):
        return len(self.cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}({len(self)})"

    def __repr__(self):
        return str(self.cards)


    def __add__(self, other):
        my_type = type(self)
        print(my_type)
        tmp = my_type(self.dealer) # tmp = CardDeck(...)
        tmp._cards = self.cards + other.cards
        return tmp
