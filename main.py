"""
Main module.
"""
import map_builder
import database


def main():
    """
    Run the application
    """
    year = int(input('\nPlease enter a year you would like to have a map for: \n'))
    user_location = input('Please enter your location (format: lat, long): \n')
    print('\n***** Please, keep in mind that the original database is too big, so it would\
 take 14 days analyze it completely. ***** \n')
    lines_to_read = int(
        input("Choose how many lines of data would you like to proceed in range from 10 to 1241772: \n"))
    user_location = (float(user_location.split(
        ',')[0]), float(user_location.split(',')[1]))
    print('Your map is generating...\n')
    result = database.read_file('locations.list', lines_to_read)
    print('Please wait... 10% complete\n')
    films_by_year = database.find_year(result, year)
    print('Please wait... 20% complete\n')
    locations = database.get_coordinates(films_by_year)
    print('Please wait... 50% complete\n')
    locations = database.find_distance(locations, (user_location))
    map_builder.build_map(locations, user_location, year)
    map_name = str(year) + '_movies_map.html'
    print("Finished. Please have look at the map ", map_name)


if __name__ == "__main__":
    main()
