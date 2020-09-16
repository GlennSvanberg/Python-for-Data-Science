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
