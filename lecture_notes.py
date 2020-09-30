table = [None] * 8


class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"HashEntry({repr(self.key)}, {repr(self.value)})"


def hashf(s):
    """NAIVE HASHING FUNCTION -- DO NOT USE!!!"""
    total = 0

    bytes = str(s).encode()

    for b in bytes:  # O(n) over the length of the key/string (s) -- size of the table does not affect this
        total += b

    # for c in s:
        # print(c, ord(c))
        # total += ord(c)

    # return (f"{total}, {s}")

    return total


def get_index(s):
    value = hashf(s)

    return value % len(table)  # the length of this table is 8


def put(key, value):
    """
    O(n) - [Linear Time] - over the length (number of bytes) of the key
    O(1) - [Constant Time] - over the number of items in the table
    """
    index = get_index(key)
    table[index] = HashEntry(key, value)


def get(key):
    index = get_index(key)

    hash_entry = table[index]

    return hash_entry.value


# Put
# index = get_index("Brandon")
# table[index] = 420  # "420" is an arbitrary value, could be anything
put("Krampus", 420)

print(table)

# Put
# index = get_index("Goats")
# table[index] = 9999 # "9999" is also just arbitrary
put("Goats", 9994)

print(table)
# print(hashf("brandon"))
# print(hashf("nodnarb"))  # collision. wrong order, but still same value

print(get("Krampus"))
print(get("goAtS"))  # not case sensitive apparently..?
