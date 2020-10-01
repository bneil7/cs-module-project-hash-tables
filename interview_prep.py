'''
Add up and print the sum of the all of the minimum elements of each inner array:

[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

The expected output is given by:
4 + -1 + 9 + -56 + 201 + 18 = 175

You may use whatever programming language you'd like.

Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
'''

# loop through given array,
# check through each subarray,
# return minimum of each subarray
# add up every returned value


def sumOfInnerArrMins(arr):
    result = []  # initialize empty array/list to append returned values to
    for i in range(0, len(arr[0])):
        temp = 0
        for j in range(0, arr[i]):
            temp = temp + arr[j]
        result.append(temp)
    print(result)


print(sumOfInnerArrMins(
    [
        [8, 4],
        [90, -1, 3],
        [9, 62],
        [-7, -1, -56, -6],
        [201],
        [76, 18]
    ]
))
