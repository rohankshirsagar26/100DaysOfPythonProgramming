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

# Looping through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

# Creating empty dictionary
empty_dictonary = {}
print("empty_dictionary = ", empty_dictonary)

# Wiping out existing dictionary
programming_dictionary = {}
print("programming_dictionary = ", programming_dictionary)

# Nesting

capitals = {
  "France": "Paris",
  "Germany": "Berlin"
}

# Nesting list in a dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"]
}

# Nesting dictionary in a dictionary

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
  },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgard"],
    "total_visits": 5
  }
}

# Nesting a dictionary in a list

travel_log = [
  {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
  },
  {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgard"],
    "total_visits": 5
  }
]