#!/usr/bin/env python

travis_countries = """Armenia
Georgia
Qatar
Thailand
UK
Germany
Ecuador
Colombia""".split('\n')

heather_countries = """Qatar
UK
Germany
Portugal
Ireland
Mexico""".split('\n')

travis = set(travis_countries)
heather = set(heather_countries)

print(travis)
print(heather)

for i in range(1000000):
    heather.add('Mongolia')

heather.remove('Portugal')

print('both:', travis & heather)
print("either:", travis | heather)
print('just one:', travis ^ heather)
print('just Heather:', heather - travis)
print('just Travis:', travis - heather)

