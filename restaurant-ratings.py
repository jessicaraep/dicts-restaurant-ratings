import sys

def convert_file_to_dict (filename): 
    restaurant_file = open(filename)
    restaurant_ratings = {}
    for line in restaurant_file:
        line = line.rstrip()
        words = line.split(":")
        for word in words:
            restaurant_ratings[words[0]] = words[1]

    sorted_restaurant_ratings = sorted(restaurant_ratings.items())
    for item in sorted_restaurant_ratings:
        print "{} is rated at {}.".format(
            item[0], item[1])


    # restaurants = [item[0] for item in sorted_restaurant_ratings]
    # ratings = [item[1] for item in sorted_restaurant_ratings]

    # i = 0
    # for item in restaurants:
    #     print restaurants[i] + " is rated at " + ratings[i] + "."
    #     i += 1     

convert_file_to_dict(sys.argv[1])






# import sys

# filename = sys.argv[1]



