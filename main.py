# Functional Programming Solutions

# Pure function with immutable variables that flattens and sort an array of integers in ascending order

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

#How does this solution ensure data immutability?
    #I don't think it it does. It allows users to add, but not remove, data to the array. But that's a pretty weak definition of immutability.

#Is this solution a pure function? Why or why not?
    #Yes it's pure because it's output only relies on it's input--in this case, array values.

#Is this solution a higher order function? Why or why not?
    #Yes because it performs more than one funtion, first flattening to an array called 'arr', then sorting it.

#Would it have been easier to solve this problem using a different programming style?
    #Making a class of arrays that are flattened and sorted in OOP probably won't save time because you'll have to write out both funtions in your class anyway, then you have to add the code for invoking the class as an object later.

#Why in particular is functional programming a helpful paradigm when solving this problem?
    #We're treating this array of numbers as a prettty one-dimensional object, so funtional programming handles it with ease and is more direct, readable, and parsimonious.

#Object-Oreiented Programming Solutions

# General Podracer class defined with attributes: max_speed, condition (perfect, trashed, repaired) and price 

class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Repair() method that updates the condition of a podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
# AnakinsPod class inherits the Podracer class, and has a unique "boost" method that multiplies max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def boost(self):
    self.max_speed *= 2
    
# SebulbasPod class inherits the Podracer class, and has a unique "flame_jet" method that updates the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def flame_jet(self, other):
    other.condition = "trashed"

#How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    # Polymorphism: Individual pod classes inherit the same keys as the general pod class, though they aren't identical
    # Iheritance: Individual pod classes use the same keys (code) as the general pod class
    # Abstraction: Individual pod code doesn't write out the code shared with the general pod class
    # Encapsulation: Each pod class bundles together key/values pairs to make multi-dimensional programming object

#Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    # No. Using functional programming to manipulate each of these key/values pairs, and keep them bundled together in the right way for theor repective objects, would take a lot more code.

#How in particular did Object Oriented Programming assist in the solving of this problem?
    #Encapsulation enables us to easil make multi-dimensional programming objects, and inheritance enables us to avoid rewiting code for each objects
