import mymodule

print("import mymodule: ", mymodule.my_value)

# 2) from <module> import *
from mymodule import *

print("from mymodule import *: ", my_value)

# 3) from <module> import <func> as <alias name/shortened name>
from mymodule import my_value as myval

print("from mymodule import my_value as myval: ", myval)

# 4) import module with alias
import mymodule as mymod

print("import mymodule as mymod: ", mymod.my_value)
