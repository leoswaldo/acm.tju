#!/python3/bin/python3

# Because of its age, the City Hall has suffered damage to one of its walls.
# A matrix with M rows and N columns represents the encoded image of that wall,
# where 1 represents an intact wall and 0 represents a damaged wall
# (like in Figure-1).
# 1110000111
# 1100001111
# 1000000011
# 1111101111
# 1110000111
# Figure-1
#
# To repair the wall, the workers will place some blocks vertically into the
# damaged area. They can use blocks with a fixed width of 1 and different
# heights of {1, 2, ..., M}.
#
# For a given image of the City Hall's wall, your task is to determine how many
# blocks of different heights are needed to fill in the damaged area of the
# wall, and to use the least amount of blocks.
#
# Input
#
# There is only one test case. The case starts with a line containing two
# integers M and N (1 ≤ M, N ≤ 200). Each of the following M lines contains a
# string with length of N, which consists of "1" s and/or "0" s. These M lines
# represent the wall.
#
# Output
#
# You should output how many blocks of different heights are needed. Use
# separate lines of the following format:
#
# k Ck
#
# where k∈{1,2, ..., M} means the height of the block, and Ck means the amount
# of blocks of height k that are needed. You should not output the lines where
# Ck = 0. The order of lines is in the ascending order of k.
#
# Sample Input
#
# 5 10
# 1110000111
# 1100001111
# 1000000011
# 1111101111
# 1110000111
#
# Sample Output
#
# 1 7
# 2 1
# 3 2
# 5 1


def city_hall(cols, rows, wall_matrix):
    # Create the fixes dict, it will store the the fixes in the wall,
    # and it will help us to access to it throgh the key and add 1 to its value
    fixes = {}

    # We have to iterate through all matrix (wall), for that we need to create
    # 2 loops (one for rows, and other for cols)
    for row_level in range(0, rows):
        for col_level in range(0, cols):
            # Verify if the current fix needs to be fixed (0)
            if(wall_matrix[row_level][col_level] == 0):
                fixed_blocks = 1
                # Iterate from current row to down and see the ones need fix
                # in the same col, until you find one does not requires, then
                # break and save the number of fixes
                for row_level_fixed in range(row_level + 1, rows):
                    if(wall_matrix[row_level_fixed][col_level] == 0):
                        wall_matrix[row_level_fixed][col_level] = 1
                        fixed_blocks += 1
                    else:
                        break

                # see if the current number of fixes already exists
                fix = fixes.get(fixed_blocks)

                # NOTE: the number of fixed blocks is the key, and the value
                # makes reference to the number of how many times that amount
                # of fixed blogs have been found

                # In case the key is not in the dict 'fix' we will set it to 1
                # otherwise add 1 to it
                if(not fix):
                    fix = 1
                else:
                    fix += 1

                # save/update the fixes
                fixes[fixed_blocks] = fix

    #print the results
    for key, val in fixes.items():
                    print(str(key) + " " + str(val))


# Test Scenarios
cols = 10
rows = 5
wall_matrix = [[1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
              [1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
              [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
              [1, 1, 1, 0, 0, 0, 0, 1, 1, 1]]

city_hall(cols, rows, wall_matrix)
