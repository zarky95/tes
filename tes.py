x = "awesome"
def myfunc() :
    global x
    x = "fantastic"
    print ("phyton is " + x)


myfunc()

print("phyton is " + x)

import random

print(random.randrange(1, 10))

i = 1
while i < 10:
  print(i)
  i += 3
  
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

def my_func(x):
  return list(dict.fromkeys(x))

mylist = my_func(["a", "b", "a", "c", "c"])

print(mylist)
