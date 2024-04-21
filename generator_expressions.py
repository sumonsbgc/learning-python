""" 
These are a concise way to create lists. 
They can also be used to iterate over existing lists while performing operations on each element
"""
numbers = [1, 2, 3, 4, 5]
squared_generator = (x ** 2 for x in numbers)

print(squared_generator);
print(next(squared_generator));
print(next(squared_generator));
print(next(squared_generator));
print(next(squared_generator));
print(next(squared_generator));
# print(next(squared_generator));



class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
