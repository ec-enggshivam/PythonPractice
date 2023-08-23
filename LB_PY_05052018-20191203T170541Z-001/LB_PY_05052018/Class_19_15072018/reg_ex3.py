# Extract all capital lettered words from a string

import re
'''
st = input('Enter a string with Capital words: ')
pat = r'\b[A-Z]+\b'
words = re.findall(pat,st)
print(words)



st = input('Enter the string: ')
pat = r'\b[A-Z]\w+\b'
words = re.findall(pat,st)
print(words)


s="hi we know 4, 56 Python 34support 1234 regex support456 and it has 67890 0 78 two version."
pt=r"\b((?:\d\d)+)\b"

match=re.findall(pt,s,re.I)
if match:
    print("Match found: ",match)
else:
    print("No match")


s="hi we know 4, 56 Python 9876 543 210 1234 567 890 8976 345 201 regex support456 and it has 67890 0 78 two version."

pt=r"(?:[7-9]\d{3})\s(?:\d{3})\s(?:\d{3})"

match=re.findall(pt,s,re.I)
if match:
    print("Match found: ",match)
else:
    print("No match")
'''


s="hi we know 4, 56 Python AMMPA1652D AM12MPA52D AMMPD4512X  AMMPA1252DA 9876 543 210 1234 567 890 8976 345 201 regex support456 and it has 67890 0 78 two version."
pt=r"\b([A-Z]{5}\d{4}[A-Z])\b"
match=re.findall(pt,s,re.I)
if match:
    print("Match found: ",match)
else:
    print("No match")