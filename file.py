""" 
r => read => Opens a file for reading, error if the file does not exist
w => write => Opens a file for appending, creates the file if it does not exist
a => append => Opens a file for writing, creates the file if it does not exist
x => create/execute => Creates the specified file, returns an error if the file exists

===========================
Mode: 
===========================
t => text mode
b => binary mode
"""

file = open('./cast.py', 'r');

file.read();
file.readline();
file.readlines();

file.write()
file.writelines()
# file
# for ch in file:
#   print(ch)

file.close()
print(file);