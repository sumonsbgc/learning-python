""" 
These are a concise way to create lists. 
They can also be used to iterate over existing lists while performing operations on each element

[output for item in items]
"""
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]


for item in range(10):
  print(item)