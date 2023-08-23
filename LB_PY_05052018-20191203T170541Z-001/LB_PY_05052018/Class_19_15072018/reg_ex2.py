import re

s="hi 113 hello hey0d 3 6 how are you4 1254458 nmks 67 yrhddnl6 78 787 1hryr5 ur241!"

pat=r'\b\d+\b'
match=re.findall(pat,s)
if match:
    print(match)
else:
    print("No match found")
'''
pat='\D'
match=re.findall(pat,s)
if match:
    print(match)
else:
    print("No match found")
'''




