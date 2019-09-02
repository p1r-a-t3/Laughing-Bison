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


def hex_to_binary(hex_value: str):
    bin_list = list()

    for chars in hex_value:
        decimal_value = int(chars, base=16)
        binary_value = str(bin(decimal_value))[2:]
        bin_list.append(binary_value)

    # zero padding
    for vals in range(0, len(bin_list)):
        number_of_zeros = 8 - len(bin_list[vals])
        bin_list[vals] = ("0" * number_of_zeros) + bin_list[vals]
    return bin_list


def xor_cipher(encrypted_text: list, binary_key: list):
    best_score = -100
    best_text = ""
    all_decrypted_text = list()

    for key in binary_key:
        decrypted_text = ""
        for text in encrypted_text:
            xored_value = ""
            for i in range(0, len(text)):
                xor = int(key[i]) ^ int(text[i])
                xored_value += str(xor)
            decimal_conversion = int(xored_value, base=2)
            decrypted_text += chr(decimal_conversion)
        all_decrypted_text.append(decrypted_text)

    for text in all_decrypted_text:
        score = scoring_system(text)
        
        if score > best_score:
            best_score = score
            best_text = text
            
    print("Best score is: {} and text is {}".format(best_score, best_text))


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
    binary_encrypted_text = hex_to_binary(
        "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

    xor_cipher(binary_encrypted_text, key)
