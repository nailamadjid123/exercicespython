def magical_cities():
    cities = {}

    while True:
        city_name = input("Enter the name of a city (or type 'stop' to finish): ")
        if city_name.lower() == "stop":
            break
        # Calculate population 
        population = len(city_name) * 1_000_000
        cities[city_name] = population

    # Sort cities by population in descending order
    sorted_cities = sorted(cities.items(), key=lambda x: x[1], reverse=True)

    

    print("\nCities and their populations (sorted by population):")
    for city, population in sorted_cities:
        print(f"{city}: {population:,} citizens")



magical_cities()
