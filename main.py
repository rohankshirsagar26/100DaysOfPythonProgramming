# Dictionary in python
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again."
}

# Retrieving item from dictionary
print(programming_dictionary["Function"])

# Adding new items to dictionary
programming_dictionary["Dictionary"] = "A set of key value pairs"

# Printing dictionary
print(programming_dictionary)

# Edit an item in dictionary
print("Bug: ", programming_dictionary["Bug"])
programming_dictionary["Bug"] = "A moth in a computer."
print("Bug: ", programming_dictionary["Bug"])