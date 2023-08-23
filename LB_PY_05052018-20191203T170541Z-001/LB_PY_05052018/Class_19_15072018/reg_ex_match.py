import re

s="Hey,.. Python is dynamic typed language"
pat="python"

'''
match=re.match(pat,s,re.I)
if match:
    print("match found:",match.group())
    print(match)
else:
    print("no match found")

match=re.search(pat,s,re.I)
if match:
    print("match found:",match.group())
    print(match)
else:
    print("no match found")
'''
s="Hey,.. Python is dynamic typed language. It comes in two version pythON2.7 and PyThon3.6"
pat="python3.6"
match=re.findall(pat,s,re.I)
if match:
    print("Matched values",match)
else:
    print("No match found")
