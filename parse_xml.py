#!/usr/bin/env python

import lxml.etree as ET

doc = ET.parse('buildings.xml')

root = doc.getroot()

print(root)

for building in root.findall('building'):
    name = building.get('building_name')
    size = int(building.find('size').text)
    print(name, size, size, building.tag)


for building in doc.findall('.//building'):
    print(building.get('building_name'))
print('-' * 60)


doc = ET.parse('DATA/solar.xml')

for planet in doc.findall('.//planet'):
    print(planet.get('planetname'))
    for moon in planet.findall('moon'):
        print('\t' + moon.text)




