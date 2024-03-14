country = input("Input Country:\n")
visits = int(input("Input number of visits:\n"))
list_of_cities = eval(input("Input cities: [\"city1\", \"city 2\", ...]\n"))

travel_log = [
    {
        "country":"France",
        "visits": 12,
        "cities": ["Paris","Lille", "Dijon"]
    },
    {
        "country":"Germany",
        "visits": 5,
        "cities":["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country,visits,list_of_cities):
    new_country ={}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = list_of_cities
    travel_log.append(new_country)

add_new_country(country,visits,list_of_cities)
print(travel_log[-1])
