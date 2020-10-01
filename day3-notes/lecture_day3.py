
## What Hash Table Solve ##
#
# * We need to look up some data quickly
# * SOme data that was slow to generate or obtain
#
# In lieu of linear search...
#
# It doesn't matter if _n_ is small. O(n) vs O(1)
#
# * Any time-consuming process:
#
# * Memoization (caching)
# * Network caching
# * Indexing
# * Removing duplicates from lists
# * Detecting duplicates
# * Counting duplicates

# NAIVE FIBONACCI
# 0 1 1 2 3 5 8 13 21 34 55 ... <-- this is O(n), looking at prev 2 numbers and adding them together
# recursive definition of fibonacci:
# fib(0): 0
# fib(1): 1
# fib(n): fib(n-1) + fib(n-2)
#
cache = {}  # speeds things way up


def fib(n):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)

    return cache[n]


for i in range(100):
    print(f"{i:3} {fib(i)}")


# def foo(a, x, b):

#     cache[(a, x, b)] = ...
