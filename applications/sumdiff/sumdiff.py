"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


cache = {}
sums = {}
diffs = {}
# nested for loop
for i in q:  # the index
    for j in q:  # the value
        add = f(i) + f(j)
        if add in sums:
            # append values
            # stored in tuples so the values cannot be changed
            sums[add].append((i, j))
        else:
            sums[add] = [(i, j)]

        sub = f(i) - f(j)
        if sub in diffs:
            diffs[sub].append((i, j))
        else:
            diffs[sub] = [(i, j)]

for w in sums:
    if w in diffs:
        for v in sums[w]:
            for y in diffs[w]:
                a, b = v[0], v[1]
                c, d = y[0], y[1]
                assert(f(a) + f(b) == f(c) - f(d))
                print(
                    f'f({a}) + f({b}) = f({c}) - f({d})      {f(a)} + {f(b)} = {f(c)} - {f(d)} ')
