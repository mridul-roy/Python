travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited,times_visited,cities_visited):
    add_country ={}
    add_country["country"] = country_visited
    add_country["visits"] = times_visited
    add_country["cities"] = cities_visited

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
