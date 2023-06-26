class Item:
    # down here, we've made put in these extra parameters (apart from self - which is there, to let the method know, for which instance its being executed for) to make them a requirement for creating an instance...
    # important side-notes: just because we're using the __init__ method doesn't mean that we can't differentiate b/w mandatory & non-mandatory parameters...
    # eg. if we don't know know the quantity for an item, then we set a default value inside the method itself, thereby making the parameter optional...
    def __init__(self, name, price, quantity=0):
        # what we've done now is define the attributes for each instance dynamically using the "self" parameter (because we know how self works in python from the previous file/example)
        # note for self - the stuff on the left {self.name,price,quantity} are the attributes and the stuff on the right are the parameters that the method receives from the instances...
        self.name = name
        self.price = price
        self.quantity = quantity
        # it's best practice to assignment the attributes inside the constructor

    # we don't really need the x & y parameters anymore, as we know that for each method that we design for classes, the object itself is passed as an argument (I know I'm repeating this over & over again, but really this is the most important part) {and as the instance itself is passed as an argument, thus we use "self" in the methods}
    def calculate_total_price(self):
        # the reason we're able to do this is because, we assigned these attributes to the instances the moment they were created using the constructor & these attributes are accessible to us throughout the methods that we create under this specific class... :D
        return self.price * self.quantity

# In terms of best practices in OOP, there are few problems that we've done here (below)

# 1. There aren't any set of rules for the attributes that we would like to pass in to instantiate an instance successfully.
# Meaning, what we've done here is hardcoded each attribute (i.e - for every item {item1, item2, item3, item4...} we would have to type in the attribute each time we create an instance TT_TT)

# Proposition:
# What if we could declare in a class that for every instance that we create, name, price & quantity must be passed.

# create constructor functions: (why?)
# Solution => create a special method - (__init__) == constructor
# these methods that start & end with these double underscores (__magicMethods__) are also known as magic methods

# More about the __init__ method (constructor):
# This is something that will be always executed (per instance) if its defined a class and an instance in created.


item1 = Item("Phone", 100, 1)


item2 = Item("Laptop", 1000, 3)

# # we can also assign attributes to instances individually as well, even if they aren't in the constructor...
# item2.has_numPad = False

print(f"The total price for item 1 = {item1.calculate_total_price()}")
print(f"The total price for item 2 = {item2.calculate_total_price()}")
