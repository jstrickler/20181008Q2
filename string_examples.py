#!/usr/bin/env python

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s4 = r'''spam\n'''

print("It's convenient")
print('He is the "man"')

query = """
select *
from customers
where lastname = "smith"
"""

html_start = '''
<html>
<meta></meta>
<head></head>
<body>
'''

print("85\u00B0 in October?")

actor = "Hugh Jackman"

print(actor + ' (Wolverine)')

print("Wolverine" * 10)

print(actor.upper())
print(actor.startswith('H'))
print(actor.startswith('h'))
print(actor.lower().startswith('h'))

print(actor.lower())
print(actor.lower)
print(dir(actor.lower))
print(type(actor.lower))

print(id(actor))

#  print(actor.id())

print(len(actor))
print(actor.__len__())


print(__builtins__)

print(dir(__builtins__))
print(dir(dir))

print(actor.count('a'))

s = """
  
  
  \t\t  All my exes live in Texas  \t\t   
  
  """
print('|' + s.lstrip() + '|')
print('|' + s.rstrip() + '|')
print('|' + s.strip() + '|')
print()

s = 'xyxxyyxxxyyy All my exes live in Texasxxxyyyxyxyx'

print('|' + s.lstrip('xy') + '|')
print('|' + s.rstrip('yx') + '|')
print('|' + s.strip('xy\x17') + '|')

s = 'fee fi fo fum'

words = s.split()
print(words)

words = s.partition(' ')
print(words)

s = 'fee:fi:fo:fum'
print(s.split(':'))
print(s.rsplit(':', 2))
print(s.rsplit(':', 2))




























