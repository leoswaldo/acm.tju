# [3780. How Many Islands?]

### Description

You are given a marine area map that is a mesh of squares, each representing
either a land or sea area. Figure B-1 is an example of a map.

    10100
    10000
    10101
    10010

Figure B-1 (UP): A marine area map


You can walk from a square land area to another if they are horizontally,
vertically, or diagonally adjacent to each other on the map. Two areas are on
the same island if and only if you can walk from one to the other possibly
through other land areas. The marine area on the map is surrounded by the sea
and therefore you cannot go outside of the area on foot.

You are requested to write a program that reads the map and counts the number
of islands on it. For instance, the map in Figure B-1 includes three islands.

### Input

The input consists of a series of datasets, each being in the following format.

    w h
    c1,1 c1,2 ... c1,w
    c2,1 c2,2 ... c2,w
    ...
    ch,1 ch,2 ... ch,w


w and h are positive integers no more than 50 that represent the width and the
height of the given map, respectively. In other words, the map consists of w×h
squares of the same size. w and h are separated by a single space.

ci, j is either 0 or 1 and delimited by a single space. If ci,j = 0, the square
that is the i-th from the left and j-th from the top on the map represents a sea
area. Otherwise, that is, if ci, j = 1, it represents a land area.

The end of the input is indicated by a line containing two zeros separated by a
single space.


### Output

For each dataset, output the number of the islands in a line. No extra
characters should occur in the output.

### Sample Input

    1 1
    0
    2 2
    0 1
    1 0
    3 2
    1 1 1
    1 1 1
    5 4
    1 0 1 0 0
    1 0 0 0 0
    1 0 1 0 1
    1 0 0 1 0
    5 4
    1 1 1 0 1
    1 0 1 0 1
    1 0 1 0 1
    1 0 1 1 1
    5 5
    1 0 1 0 1
    0 0 0 0 0
    1 0 1 0 1
    0 0 0 0 0
    1 0 1 0 1
    0 0


### Sample Output

    0
    1
    1
    3
    1
    9


[3780. How Many Islands?]:http://acm.tju.edu.cn/toj/showp3780.html