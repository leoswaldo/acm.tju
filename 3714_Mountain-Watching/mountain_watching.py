#!/python3/bin/python3


## Function: finde_widest_mountain
#  Description: find the widest mountain in the valley, based on height of the
#      mountains
#  Parameters: mountains_heights
#       mountains_heights: valley (height of the mountains)
def find_widest_mountain(mountains_heights):
    # set default values to variables
    max_wide = 0
    current_wide = 0
    last_height = 0
    equal_height = 1
    down = False

    # iterate through all heights of valley
    for height in mountains_heights:
        if(height > last_height):
            # if the valley comes from down the hills then assign proper value
            # to current wide, otherwise keep growing
            if(down):
                current_wide = equal_height + 1
                down = False
            else:
                current_wide = current_wide + 1
            # assing equal height to one since the height is not repeated
            equal_height = 1
        else:
            # verify if the height is being repeated to know if after we'll add
            # it to a new mountain
            if(last_height == height):
                equal_height += 1
                current_wide += 1
            else:
                # we raised the flag indicating that the flow of the valley
                # went down the hills
                down = True
                current_wide += 1
                equal_height = 1

        last_height = height

        # compare the current wide with the max wide found, if bigger then
        # assign it
        if(current_wide > max_wide):
            max_wide = current_wide

    return max_wide


if(__name__ == '__main__'):
    #mountains = [3, 2, 3, 5, 4, 1, 6]
    #mountains = [2, 1, 2, 3, 4, 5, 3, 1, 1, 2, 1]
    #mountains = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 1, 2, 3]

    mountains = [3, 2, 1, 1, 1, 1, 2, 3, 3, 3, 6, 7, 7, 7, 7, 7, 7, 7,
        6, 5, 4, 3, 3, 3, 2, 1, 1, 1, 1, 1, 2, 3, 4, 4, 4, 5, 6, 7, 6, 5, 4,
        3, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 3, 4, 3, 2, 3, 2, 1, 1, 1, 1,
        1, 1, 2, 1, 1]

    print(find_widest_mountain(mountains))