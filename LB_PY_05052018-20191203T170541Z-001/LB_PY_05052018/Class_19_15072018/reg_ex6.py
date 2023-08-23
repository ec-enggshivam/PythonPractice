import re

line = "This is Learnbay This + 5674 CLASS 4782 This"
searchObj = re.search( r'([1-9]+).*', line,re.I|re.S)
if searchObj:
    print ("search --> searchObj.group() : ", searchObj.group())
else:
    print ("Nothing found!!")

line = "This is Learnbay This + 5674 CLASS 4782 This"
searchObj = re.search( r'([1-9]+).?', line,re.I|re.S)
if searchObj:
    print ("search --> searchObj.group() : ", searchObj.group())
else:
    print ("Nothing found!!")

line = "This is Learnbay class1 class2 class3 5674 CLASS 4782 This";
searchObj = re.search( r'(class[0-9]).*', line)
if searchObj:
    print ("search --> searchObj.group() : ", searchObj.group())
else:
    print ("Nothing found!!")

line = "123123123123"
srchObj = re.search("(\d\d\d)\\1{1}",line)
if srchObj:
    print( line)
    print (srchObj.group())

line = "akakankn 123123123123 amkamxmaxmxalm"
srchObj = re.search("(\d\d\d).*",line)
if srchObj:
    print( line)
    print (srchObj.group())

line = "This is Learnbay class1 class2 class3 5674 CLASS 4782 This";
searchObj = re.search( r'(Learnbay.*[0-9]).*', line)
if searchObj:
    print ("search --> searchObj.group() : ", searchObj.group())
else:
    print ("Nothing found!!")


line = "is This is Learnbay 123 456 hi 789 Class this This is"
searchObj = re.findall( r'(\d\d\d)+', line)
if searchObj:
    print ("search --> searchObj.group() : ", searchObj)
else:
    print("Nothing found!!")

line = "is This is Learnbay 123 456 hi 789 Class this This is"
searchObj = re.findall( r'[4-6][4-6][4-6]', line)
if searchObj:
    print ("search --> searchObj.group() : ", searchObj)
else:
    print("Nothing found!!")

line = "is This is Learnbay 123 456 hi 789 192.168.254.001 Class this This is"
searchObj = re.findall( r'[0-2][0-9][0-5]', line)
if searchObj:
    print ("search --> searchObj.group() : ", searchObj)
else:
    print("Nothing found!!")
