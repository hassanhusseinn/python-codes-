import random
import string 
import datetime #this is for the date and time

#this module is for math operations

def add(a, b):
  return a + b
  

haha = add(1, 2) #this will return 3
print (haha)




letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

rand = random.choices(letters, k=10)
print(rand)


current = datetime.datetime.now()
print(current)








