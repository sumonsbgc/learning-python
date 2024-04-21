"""
Loop control statements:
break: Terminates the loop prematurely and transfers execution to the statement immediately following the loop.
continue: Skips the rest of the code inside the loop for the current iteration and proceeds to the next iteration.
pass: Acts as a placeholder. It does nothing and allows the code to pass without throwing an error.
"""

# for ... in
sequence = []
for item in sequence:
  print(item)

for item in range(10):
  print(item)

# while
i = 0
while i < 5:
  print(i)
  i+=1

# while ... else
i = 0
while i < 5:
  print(i)
  i+=1
else:
  print('Done')
  
# enumerate
fruites = ['Lichi', 'Guaba', 'PineApple']
for index, item in enumerate(fruites):
  print(index, item)

# zip
prices = [400, 140, 230]
for item, price in zip(fruites, prices):
  print(price, item)
