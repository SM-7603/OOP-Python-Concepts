# Regular Variables: (different datatypes)
item1 = "Phone"
item1_price = 100
item1_quantity = 5
item1_total_price = item1_price * item1_quantity

# Now, we're printing out the datatype of the variables...
print(type(item1))  # str
print(type(item1_price))  # int
print(type(item1_quantity))  # int
print(type(item1_total_price))  # int
# Here, we notice that the result is <class 'dataType'>
# Pay special attention to the key-word "class"...as we get it along side the dataTypes...
# We get this because, the dataTypes are the instances of the "str" or "int" in the above case...
# That's because, each dataType in python is an object that has been instantiated earlier by some class. And for the variable "item1" that has been instantiated from a class named "str" & for the other 3 variables they have been instantiated from a class named "int".
# Now, each instance could have attributes that will contain information related to it.  
