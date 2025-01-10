class Animal:
  def __init__(self,name):
    self.name = name
    
  def eat(self):
    print(f"{self.name} is eating!")
    
  def make_sound(self):
    print(f"{self.name} makes a sound")
    
  def walk(self):
    print(f"{self.name} is walking")
    
  def run(self):
    print(f"{self.name} is running")
    
class Dog(Animal):
  def make_sound(self):
    print(f"{self.name} is barking")
  
  def run(self):
    print(f"{self.name} is running")
class Cat(Animal):
  def make_sound(self):
    print(f"{self.name} is meowing")
  
  def walk(self):
    print(f"{self.name} is walking")