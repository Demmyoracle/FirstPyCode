countries = [['Egypt', 'USA', 'India'], ['Dubai', 'America', 'Spain','Egypt'], ['USA','London', 'England', 'France']]
countries2  = [country for sublist in countries for country in sublist if len(country) < 7]
print(countries2)
print("First code---")