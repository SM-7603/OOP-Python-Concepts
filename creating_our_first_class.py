# Keep this in mind: creating the instance == creating an object


# 1st part: Create the class

class Item:
    def calculate_total_price(self, x, y):
        return x * y


# 2nd part: Create the instance of the class
item1 = Item()
# create attributes to one instance of the class
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
# the way these are different from regular variables we created in intro_oop.py is in this way: all of these have a relationship, as these attributes are assigned to one instance of the class (therefore connecting them).
# calling & printing the method for item1
print(item1.calculate_total_price(item1.price, item1.quantity))

# create another instance of Item:
item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
# calling & printing the method for item2
print(item2.calculate_total_price(item2.price, item2.quantity))

# calling the method
# item2.calculate_total_price()  # so what's happening here?
# 1.We're calling the method from the instance "item2" and what Python does is, it passes the object "item2" itself as the 1st argument every-time...
# 1.5 The reason it does so, is to let the method know that its being used for the instance "item2".
# 2. This is the reason why methods must always have a parameter...
# The above 2 reasons are why we use "self" as a parameter for our methods, you could call it anything (it doesn't have to be "self") but it's convention to do so.


# # Print to check the dataType of the variables:
# print(type(item1))  # item
# # Notice how the dataType of item1 is now item (that's different from before)
# print(type(item1.name))  # str
# print(type(item1.price))  # int
# print(type(item1.quantity))  # int

# # # this example below is equivalent to creating an instance of a class {above} (in this case the class is <str>)
# # random_str = str(4)
# # print(type(random_str))

# # Checking how methods work by using the built-in class "str"
# random_str = "aaa" # creating an instance of the str class
# print(random_str.upper()) # executing the upper() method

# # So, the question now is this:
# # How to design some methods that can execute with our instances???
# # Answer - We write the methods inside our class, thereby making them accessible to our instances.
# # Also, methods are basically functions inside classes :D
