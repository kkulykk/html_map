"""
Module to build a map.
"""
import folium


def build_map(locations: list, user_location: tuple, year: int):
    """
    Generate html file with a map and markers on it.
    """
    main_map = folium.Map(location=[user_location[0],
                                    user_location[1]], zoom_start=4)
    user_loc = folium.FeatureGroup(name="Your location")
    all_markers = folium.FeatureGroup(name="All markers location", show=False)
    ten_markers = folium.FeatureGroup(name="10 nearest markers")
    user_loc.add_child(folium.Marker(
        location=[user_location[0], user_location[1]], popup='Your location',
        icon=folium.Icon(color='red')))
    for i in locations[10:]:
        all_markers.add_child(folium.Marker(
            location=[i[1][0], i[1][1]], popup=i[0], icon=folium.Icon(color='green')))
    for i in locations[:10]:
        ten_markers.add_child(folium.Marker(
            location=[i[1][0], i[1][1]], popup=i[0], icon=folium.Icon()))
    main_map.add_child(user_loc)
    main_map.add_child(ten_markers)
    main_map.add_child(all_markers)
    main_map.add_child(folium.LayerControl())
    map_name = str(year) + '_movies_map.html'
    main_map.save(map_name)
