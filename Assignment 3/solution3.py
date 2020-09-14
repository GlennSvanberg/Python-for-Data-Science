"""
The aim of this problem is to write an encoder and decoder for strings. 
For the encoder, it compresses a string by replacing each consecutive sequence of the same letter by this letter and its 
frequency (example: ”bbccccccdrrrffhhhh” will be ”b2c6d1r3f2h4”). For the decoder, 
it reverses the encoder process by transforming a compressed string to its full representation.

Solve this problem by using generators and without using the groupby function.
"""
from collections import namedtuple


def encoder_list(data):
    # Compress the string by replacing each consecutive sequence of the same letter by this letter and it's frequency
    encoded = []
    char_count = 1
    prev_char = ""
    for index, char in enumerate(data):
        if char == prev_char:
            char_count += 1
        else:
            if index != 0:
                res = prev_char + str(char_count)
                encoded.append(res)
                char_count = 1
            prev_char = char

        if index == len(data) - 1:
            encoded.append(prev_char + str(char_count))
    return "".join(encoded)


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
        print(x)
        res = res + f"{x[0]}{x[1]}"
    return res


def decoder_generator(data):
    pass


def decoder(data):
    # reverse the compression
    return data


data = "bbccccccdrrrffhhhh"
print(data)


print(encoder_list(data))
encoded = encoder(data)
print(encoded)
decoded = decoder(encoded)
print(decoded)
