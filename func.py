
# FUNCTION WITH PASS BY VALUE ARG:
def sayHello(name: str):
  return "Hello " + name


# FUNCTION PASS KEYWORD ARGS (kwargs):
def getKewWardArgs(**kwargs):
  return kwargs

print(getKewWardArgs(a=10, b=29))

# FUNCTION WITH TUPLE ARG:
def getTotal(*arg: int):
  return len(arg);
  # return sum(arg);

print(getTotal(29,4,64))

# LAMBDA FUNCTION -> lambda arguments: expression

add = lambda x,y: x+y
print(add(20, 30))