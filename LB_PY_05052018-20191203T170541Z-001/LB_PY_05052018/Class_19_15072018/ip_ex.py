import re


#0.0.0.0
#255.255.255.255
#(((1-255.)(1-255.)(1-255.))(1-255))

#fetch IP address
st = input('Enter the string: ')
#pat = r'\b[1-9]\b|\b[1-9][0-9]\b|\b[1][0-9][0-9]\b|\b[2][0-4][0-9]\b|\b[2][0-5][0-5]\b'
# (1-9|10-99|100-199|200-249|200-255)
pat = r'\b((?:(?:[1-9]\b|\b[1-9][0-9]\b|\b[1][0-9][0-9]\b|\b[2][0-4][0-9]\b|\b[2][0-5][0-5])\.){3}(?:(?:[1-9]\b|\b[1-9][0-9]\b|\b[1][0-9][0-9]\b|\b[2][0-4][0-9]\b|\b[2][0-5][0-5])\b))\b'
words = re.findall(pat,st)
print(words)