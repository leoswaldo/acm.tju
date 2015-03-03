# [3714. Mountain Watching]


### Problem Description
One day, Bessie was gazing off into the distance at the beautiful Wisconsin
mountains when she wondered to herself: which mountain is the widest one?

She decided to take N (1 ≤ N ≤ 100,000) equally-spaced height measurements Hi
(1 ≤ Hi ≤ 1,000,000,000) sequentially along the horizon using her new Acme Long
Distance Geoaltimeter.

A mountain is defined to be a consecutive sequence of H_i values which
increases (or stays the same) and then decreases (or stays the same),
e.g., 2, 3, 3, 5, 4, 4, 1. It is possible for a mountain on the edge of her
field of vision only to increase or only to decrease in height, as well.

The width of a mountain is the number of measurements it encompasses. Help
Bessie identify the widest mountain.


Here's a simple example of a typical horizon:

<code>
           *******                   *
          *********                 ***
          **********               *****
          ***********           *********               *
*      *****************       ***********             *** *
**    *******************     *************   * *     *******      *
**********************************************************************
</code>
3211112333677777776543332111112344456765432111212111112343232111111211
aaaaaa                   ccccccccccccccccccccc eeeeeee    ggggggggg
  bbbbbbbbbbbbbbbbbbbbbbbbbbbb             ddddd ffffffffff  hhhhhhhhh


The mountains are marked 'a', 'b', etc. Obviously, mountain b is widest with
width 28. The mountain on the left has width 6 for the purposes of this task.

### Input

+ Line 1: A single integer: N

+ Lines 2..N+1: Line i+1 contains a single integer: Hi

### Output

+ Line 1: A single line with a single integer that is the width of the widest mountain.

### Sample Input

    7
    3
    2
    3
    5
    4
    1
    6

### Sample Output

    5

Hint

The height measurements are 3, 2, 3, 5, 4, 1, 6. The widest mountain consists
of the measurements 2, 3, 5, 4, 1. Other mountains include 3, 2 and 1, 6


[3714. Mountain Watching]:http://acm.tju.edu.cn/toj/showp3714.html