"""
The aim of this problem is to write an encoder and decoder for strings. 
For the encoder, it compresses a string by replacing each consecutive sequence of the same letter by this letter and its 
frequency (example: ”bbccccccdrrrffhhhh” will be ”b2c6d1r3f2h4”). For the decoder, 
it reverses the encoder process by transforming a compressed string to its full representation.

Solve this problem by using generators and without using the groupby function.
"""


def encode_generator(data):
    char_count = 1
    prev_char = ""
    for char in data:
        res = ()
        if prev_char == "":
            prev_char = char
            continue
        if char == prev_char:
            char_count += 1
        else:
            res = (prev_char, char_count)
            char_count = 1
            prev_char = char
            yield res
        res = (prev_char, char_count)
    yield res


def encoder(data):
    res = ""
    for x in encode_generator(data):
        res = res + f"{x[0]}{x[1]}"
    return res


def decoder_generator(data):
    is_letter = True
    current_char = ""
    nr = 0
    for char in data:
        if is_letter:
            is_letter = False
            current_char = char
        else:
            is_letter = True
            nr = int(char)
            seq = ""
            for n in range(nr):
                seq = seq + current_char
            yield seq


def decoder(data):
    res = ""
    for x in decoder_generator(data):
        res = res + x
    return res


data = "bbccccccdrrrffhhhh"
print(data)

encoded = encoder(data)
print(encoded)

decoded = decoder(encoded)
print(decoded)
