#!/usr/bin/env python

# import xml.etree.ElementTree as ET
import lxml.etree as ET

buildings = ET.Element('buildings', category='office')

data = [
    ('Berrington', 40000),
    ('Radford', 60000),
    ('Plaza', 75000),
]

for building, size in data:
    e = ET.SubElement(buildings, 'building', building_name=building)
    ET.SubElement(e, 'size').text = str(size)

print(ET.tostring(buildings, pretty_print=True).decode())

doc = ET.ElementTree(buildings)

xml = ET.tostring(buildings, pretty_print=True).decode()

doc.write('buildings.xml', pretty_print=True, xml_declaration=True, encoding='UTF-8')


