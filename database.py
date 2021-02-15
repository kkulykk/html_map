"""
Module to work with database file.
"""

import math
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderUnavailable
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="html_map")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)


def read_file(file_name: str, lines_to_read: int) -> list:
    """
    Read the given amount of lines of file and return the information.
    >>> read_file('locations.list', 1)
    [['"#1 Single" (2006)', 'Los Angeles, California, USA']]
    """
    result = []
    with open(file_name, 'r', errors='ignore') as file:
        for k, line in enumerate(file):
            info = line.strip().split('\t')
            movie = [j for j in info if j != '']
            result.append(movie)
            if k == lines_to_read - 1:
                break
    return result


def find_year(result: list, year: int) -> list:
    """
    Return a list of films made only in specific year.
    >>> find_year(['"#1 Single" (2006)', 'Los Angeles, California, USA'], 2005)
    []
    >>> find_year(read_file('locations.list', 1), 2006)
    [['"#1 Single" (2006)', 'Los Angeles, California, USA']]
    """
    films_by_year = []
    for i in result:
        if f'({year})' in i[0]:
            films_by_year.append(i)
    return films_by_year


def get_coordinates(films_by_year: list) -> list:
    """
    Find coordinates to a locations where films were made.
    >>> get_coordinates([['"#1 Single" (2006)', 'Los Angeles, California, USA']])
    [['"#1 Single" (2006)', (34.0536909, -118.242766)]]
    """
    locations = []
    for i, film in enumerate(films_by_year):
        try:
            location = geolocator.geocode(film[1])
        except GeocoderUnavailable:
            continue
        if location is None:
            continue
        locations.append(
            [films_by_year[i][0], (location.latitude, location.longitude)])
    return locations


def find_distance(locations: list, user_location: tuple) -> list:
    """
    Find distance between given locationa and a place where film was made.
    Return sorted by length of distance list.
    >>> find_distance([['"#1 Single" (2006)', (34.0536909, -118.242766)]],\
 (49.09138822696914, 31.264831449793594))
    [['"#1 Single" (2006)', (34.0536909, -118.242766), 10289.9882260958]]
    """
    for i in locations:
        lat1 = i[1][0]
        lat2 = user_location[0]
        lon1 = i[1][1]
        lon2 = user_location[1]
        lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
        distance = 2 * 6371 * math.asin(math.sqrt(math.sin((lat2 - lat1)/2) ** 2 +
                                                  math.cos(lat1) * math.cos(lat2) *
                                                  math.sin((lon2 - lon1)/2) ** 2))
        i.append(distance)
    return sorted(locations, key=lambda x: x[-1])
