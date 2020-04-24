# Author: Sarah Oertly
# Date: 10/19/2019
# Description: A hailstone sequence starts with some positive integer. If that integer is even, then you divide it by
# two to get the next integer in the sequence, but if it is odd, then you multiply it by three and add one to get the
# next integer in the sequence. Then you use the value you just generated to find the next value, according to the same
# rules. For example, if our initial number is 3, the subsequent numbers will be: 10, 5, 16, 8, 4, 2, 1.
# Write a function named hailstone that takes a positive integer parameter as the initial number of a hailstone sequence
# and returns how many steps it takes to reach 1 (technically you could keep going 1, 4, 2, 1, 4, 2, etc. but you will
# stop when you first reach 1). If the starting integer is 1, the return value should be 0, since it takes no steps to
# reach 1 (we're already there). For example, if the starting integer is 3, then the sequence would go: 3, 10, 5, 16, 8,
# 4, 2, 1, and the return value should be 7, since it took 7 steps to reach 1.
# The function should just return the value, not display it (though of course you can use print statements during
# testing and debugging).
# You cannot use recursion, since we haven't covered that technique.
def hailstone(n):
    assert n > 0
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
            return 1 + hailstone(n // 2)
    else:
            return 1 + hailstone((n*3)+1)
    result = hailstone(15)
    print (result)