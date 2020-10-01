# Plaintext: HELLOWORLD
# Ciphertext: DOGGEBEUGW
# ^^^ encrypted using the encoding table dictionary
# plain: BRANDON
# cipher: ZUHCWEC
encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

decode_table = {}

for key, value in encode_table.items():  # items() method returns a list of tuples
    decode_table[value] = key


def encode(s):
    r = ""

    for c in s:
        r += encode_table[c]

    return r


def decode(s):  # had to create an empty dictionary above for a decode table
    r = ""

    for c in s:
        r += decode_table[c]

    return r


print(encode("HELLOWORLD"))
print(decode("DOGGEBEUGW"))

print(encode("BRANDON"))
print(decode("ZUHCWEC"))
