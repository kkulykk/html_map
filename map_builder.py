"""
Module to build a map.
"""
import folium
import database


def build_map(locations: list, user_location: tuple, year: int):
    """
    Generate html file with a map and markers on it.
    """
    map = folium.Map(location=[user_location[0],
                               user_location[1]], zoom_start=4)
    user_loc = folium.FeatureGroup(name="Your location")
    all_markers = folium.FeatureGroup(name="All markers location", show=False)
    ten_markers = folium.FeatureGroup(name="10 nearest markers")
    user_loc.add_child(folium.Marker(
        location=[user_location[0], user_location[1]], popup='Your location', icon=folium.Icon(color='red')))
    for i in locations[10:]:
        all_markers.add_child(folium.Marker(
            location=[i[1][0], i[1][1]], popup=i[0], icon=folium.Icon(color='green')))
    for i in locations[:10]:
        ten_markers.add_child(folium.Marker(
            location=[i[1][0], i[1][1]], popup=i[0], icon=folium.Icon()))
    map.add_child(user_loc)
    map.add_child(ten_markers)
    map.add_child(all_markers)
    map.add_child(folium.LayerControl())
    map_name = str(year) + '_movies_map.html'
    map.save(map_name)


# if __name__ == "__main__":
#     year = int(input('\nPlease enter a year you would like to have a map for: \n'))
#     user_location = input('Please enter your location (format: lat, long): \n')
#     print('\n***** Please, keep in mind that the original database is too big, so it would\
#  take 14 days analyze it completely.\nIf you choose analysing first 200 lines,\
#  it would take 2 minutes *****')
#     lines_to_read = int(
#         input("\nChoose how many lines of data would you like to proceed: \n"))
#     user_location = (float(user_location.split(
#         ',')[0]), float(user_location.split(',')[1]))
#     print('Your map is generating...\n')
#     result = database.read_file('locations.list', lines_to_read)
#     print('Please wait... 10% complete\n')
#     films_by_year = database.find_year(result, year)
#     print('Please wait... 20% complete\n')
#     locations = database.get_coordinates(films_by_year)
#     print('Please wait... 50% complete\n')
#     locations = database.find_distance(locations, (user_location))
#     build_map(locations, user_location)
#     print("Completed!")
