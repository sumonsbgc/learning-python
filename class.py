class GrandParent:
  def __init__(self) -> None:
    pass

  def getName() -> str:
    print(__class__)

class Parent(GrandParent):
  def __init__(self) -> None:
    super().__init__()
  
  def getName() -> str:
    print(__class__);


""" 
Inheritance and Multiple Inheritance
Python supports Multiple Inheritance and Multi Level Inheritance Both
"""
class Child(Parent, GrandParent):
  def __init__(self) -> None:
    super().__init__()
    
  def getName() -> str:
    print(__class__)
    
    
    
child = Child
parent = Parent
grandParent = GrandParent

parent.getName()
child.getName()
grandParent.getName()