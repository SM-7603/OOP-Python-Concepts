# Keep this in mind: creating the instance == creating an object


# 1st part: Create the class

class Item:
    pass # this is just to avoid errors for now

# 2nd part: Create the instance of the class
item1 = Item()
# create attributes to one instance of the class
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
# the way these are different from regular variables we created in intro_oop.py is in this way: all of these have a relationship, as these attributes are assigned to one instance of the class (therefore connecting them).

# Print to check the dataType of the variables:
print(type(item1))  # item
# Notice how the dataType of item1 is now item (that's different from before)
print(type(item1.name))  # str
print(type(item1.price))  # int
print(type(item1.quantity))  # int

# # this example below is equivalent to creating an instance of a class {above} (in this case the class is <str>)
# random_str = str(4)
# print(type(random_str))

# Checking how methods work by using the built-in class "str"
random_str = "aaa" # creating an instance of the str class
print(random_str.upper()) # executing the upper() method
