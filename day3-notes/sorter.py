# dictionary
d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}

items = list(d.items())

# sort by key (alphabetical in this instance)

items.sort()

for i in items:
    print(f"{i[0]}: {i[1]}")

print("---------")

# sort by value (numerical since the values are integers)

"""
def sort_by(t):
    print(f"sort_by({repr(t)}) called!")
    return t[1]


items.sort(key=sort_by)  # using the "key" parameter
"""

items.sort(key=lambda t: t[1], reverse=True)
# "lambda" is just Python's way of doing anonymous functions

for i in items:
    print(f"{i[0]}: {i[1]}")
