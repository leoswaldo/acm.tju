#!/python3/bin/python3

# A square matrix contains equal number of rows and columns. If the order of
# the matrix is known it can be calculated as in the following format:
# Order: 3
#            1 2 3
#            4 5 6
#            7 8 9
# Order: 5
#            1 2 3 4 5
#            6 7 8 9 10
#            11 12 13 14 15
#            16 17 18 19 20
#            21 22 23 24 25
#
# and so on..
#
# Now look at the diagonals of the matrices. In the second matrix - the
# elements of a diagonal are marked with circles but this is not the only one
# in this matrix but there are some other minor diagonals like <6, 12, 18, 24>
# as well as <2, 8, 14, 20> and many others.
# Input
#
# Each input line consists of two values. The first value is the order of the
# matrix and the later is an arbitrary element of that matrix. The maximum
# element of the matrix will fit as a 32-bit integer.
# Output
#
# Each output line will display the diagonal elements of the matrix containing
# the given input element.
# Sample Input
#
# 4 5
# 5 11
# 10 81
#
# Sample Output
#
# 5 10 15
# 11 17 23
# 81 92


def find_diagonals(diagonal_questions):
    # Need to know how many questions are, to iterate for each one and get its
    # answer
    questions = len(diagonal_questions)
    # Iterate for each question
    for current_question in range(0, questions):
        # Get order and number to look for
        order = diagonal_questions[current_question][0]
        number = diagonal_questions[current_question][1]
        numbers = ''
        # Iterate throug the virtual matrix to find all the diagonal members,
        # avoid breaking the limits using the order * order
        while(number < (order * order)):
            numbers += str(number) + " "
            # Add order to break line in diagonal, add 1 to make it diagonal
            # to the right
            number += order + 1

        print(numbers)

# Test scenarios
find_diagonals([[4, 5], [5, 11], [10, 81]])
