#!/usr/bin/env python

from carddeck import CardDeck

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

print(CardDeck.get_suits())

