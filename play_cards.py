#!/usr/bin/env python

from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Mitzi")

print(d1)

# print(d1.get_dealer())
#
# print(d1._dealer)
#
#
# d1.set_dealer('Fred')
#
# print(d1.get_dealer())
#
# try:
#     d1.set_dealer([])
# except TypeError as err:
#     print(err)

print(d1.dealer) # getter prop

d1.dealer = 'Bob'  # setter prop


print(d1.dealer)

try:
    d1.dealer = ['a', 'b', 'c']
except TypeError as err:
    print(err)

d1.shuffle()

print(d1.cards)

hand = []
for _ in range(5):
    hand.append(d1.draw())
print("hand:", hand)

print(d1.get_suits())

print(CardDeck.get_suits(), '\n')

j1 = JokerDeck('Albert')
j1.shuffle()
print(j1.cards)

print(j1, d1)

print(len(d1), len(j1))

print(repr(d1))

print(dir(d1))

print(len(d1))
print(CardDeck.__len__(d1))


d2 = CardDeck('Mary')

d3 = d1 + d2

print(d3)
print(len(d3))


# thing op= value
# thing = thing op value




