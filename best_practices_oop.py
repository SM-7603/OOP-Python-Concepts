class Item:
    def __init__(self):
        print("I think, therefore I am :D")

    def calculate_total_price(self, x, y):
        return x * y

# In terms of best practices in OOP, there are few problems that we've done here (below)

# 1. There aren't any set of rules for the attributes that we would like to pass in to instantiate an instance successfully.
# Meaning, what we've done here is hardcoded each attribute (i.e - for every item {item1, item2, item3, item4...} we would have to type in the attribute each time we create an instance TT_TT)

# Proposition:
# What if we could declare in a class that for every instance that we create, name, price & quantity must be passed.

# Solution => create a special method - (__init__) == constructor
# these methods that start & end with these double underscores (__magicMethods__) are also known as magic methods

# More about the __init__ method (constructor):
# This is something that will be always executed (per instance) if its defined a class and an instance in created.


item1 = Item()
# notice how - "I think, therefore I am :D" is printed 2 times, exactly when an instance is created, that's cause of the constructor...
item1.name = "Phone"
item1.price = 100
item1.quantity = 5


item2 = Item()
# notice how - "I think, therefore I am :D" is printed 2 times, exactly when an instance is created, that's cause of the constructor...
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3

# create constructor functions: (why?)
