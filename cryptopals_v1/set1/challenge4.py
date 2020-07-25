import time

# ################################
# Now that the party is jumping ##
# ################################


def get_encrypted_lines():
    encrypted_strings = list()
    with open("challenge4.txt") as f:
        for line in f.readlines():
            encrypted_strings.append(line.strip())
    return encrypted_strings


def single_char_xor():
    from challenge3_v2 import bit_combination, hex_to_byte, xor_cipher
    encrypted_lines = get_encrypted_lines()
    keys = bit_combination(8)
    fail = 0

    for encrypted_strings in encrypted_lines:
        try:
            encrypted_bytes = hex_to_byte(encrypted_strings)
            xor_cipher(encrypted_bytes, keys)
            time.sleep(2)
        except UnicodeDecodeError:
            # Only of the string is encrypted. The Rests are not encrypted.
            fail += 1
            # print("Failed {}. String: {}".format(fail, encrypted_strings))
    print("Total Fail: {}".format(fail))


if __name__ == "__main__":
    single_char_xor()
