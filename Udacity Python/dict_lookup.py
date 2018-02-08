# countries = {"india": 12}

# print(countries["US"])


def get_year_count(input):
    year_count = {}
    for key, val in input.items():
        if val in year_count:
            year_count[val] += 1
        else:
            year_count[val] = 1
    return year_count

def get_max(year_count):
    maxx = 0
    for year, count in year_count.items():
        maxx = max(maxx, count)
    return maxx

def most_prolific(input):
    """
    take a dict formatted like Beatles_Discography example above
    and return the year in which the most albums were released.
    
    """
    year_count = get_year_count(input)
    maxx = get_max(year_count)
    
    result = []
    for year, count in year_count.items():
        if count == maxx:
            result.append(year)
    
    if len(result ) == 1:
        return result[0]
    return result


Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}


print(most_prolific(Beatles_Discography))