""" 
The try: block lets you test a block of code for errors.
The except: block lets you handle the error.
The else: block lets you execute code when there is no error.
The finally: block lets you execute code, regardless of the result of the try- and except blocks.
"""

try:
  print("Try")
except NameError:
  print("Specific Error")
except:
  print("Default Error");

try:
  print("Try")
except NameError:
  print("Specific Error")
else:
  print("Default Error");

try:
  print("Try")
except NameError:
  print("Specific Error")
finally:
  print("Default Error");


""" 
To throw (or raise) an exception, use the raise keyword.
"""

raise Exception("Error Message")
raise TypeError("Error Message")
