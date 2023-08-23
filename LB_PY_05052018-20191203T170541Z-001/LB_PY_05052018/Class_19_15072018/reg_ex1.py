import re

#pat="^python"
pat="python...$" #2.7 or 3.6 ('\n')
#pat="!$"
#s="Python is dynamic typed language."
s="Python is dynamic typed language. It comes in two version pythON3.6 and PyThon2.7"
match=re.search(pat,s,re.I)
if match:
    print("match found:",match.group())
    print(match)
else:
    print("no match found")