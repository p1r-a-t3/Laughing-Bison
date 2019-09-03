import itertools


def bit_combination(n: int):
    lst = list(itertools.product([0, 1], repeat=n))

    result = list()
    for i in lst:
        unit = ""
        for t in i:
            unit += str(t)
        result.append(unit)
    return result


def codec_conversion(hex: str):
    import codecs
    # This is what means always work in bytes.
    # Do not directly convert to decimal unless otherwise needed.
    return codecs.decode(hex, "hex").decode()


def hex_to_binary(hex_value: str):
    bin_list = list()

    for chars in hex_value:
        decimal_value = int(chars, base=16)
        binary_value = str(bin(decimal_value))[2:]
        bin_list.append(binary_value)
    return bin_list


def xor_cipher(encrypted_text: list, binary_key: list):
    best_score = -100
    best_text = ""
    best_index = 0
    all_decrypted_text = list()

    for key in binary_key:
        decrypted_text = ""
        for text in encrypted_text:
            # key is in binary, text is in binary.
            # convert key to decimal.
            __key = int(str(key), base=2)
            __text = ord(text)
            # now xor
            xor = __key ^ __text  # this is xored against decimal
            # now convert this value to chr. Xored value is in decimals
            decrypted_text += chr(xor)
        # Add decrypted text in a list
        all_decrypted_text.append(decrypted_text)

    index = 0
    for text in all_decrypted_text:
        score = scoring_system(text)
        index += 1
        if score > best_score:
            best_score = score
            best_text = text
            best_index = index

    __key = binary_key[best_index]
    __key = chr(int(key, base=2))

    print("------------------------------------------------")
    print("Key in binary should be: {}".format(__key))
    print("Best score is: {}\nDecrypted Text is: {}".format(best_score, best_text))
    print("------------------------------------------------")


def scoring_system(decrypted_text: str):
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    total = 0
    for letters in decrypted_text:
        if letters in character_frequencies:
            total += character_frequencies[letters]

    return total


if __name__ == "__main__":
    key = bit_combination(8)
    binary_encrypted_text = codec_conversion(
        "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

    xor_cipher(binary_encrypted_text, key)
