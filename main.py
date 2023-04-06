# Nesting

capitals = {
  "France": "Paris",
  "Germany": "Berlin"
}

# Nesting List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"]
}

# Nesting Dictionary in a Dictionary

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

# Nesting a Dictionary in a List

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