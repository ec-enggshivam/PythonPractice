import re
# backrefferance
str = 'buttterffflyyy'

match =re.findall(r'(\w)\1{2}', str)
if match:
    print("Match found: " ,match)
else:
    print("No match")