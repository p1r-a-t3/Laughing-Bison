def get_encrypted_lines():
    encrypted_strings = list()
    with open("challenge4.txt") as f:
       for line in f.readlines():
           encrypted_strings.append(line.strip())
    return encrypted_strings


def single_char_xor():
    from challenge3 import bit_combination, codec_conversion, xor_cipher
    encrypted_lines = get_encrypted_lines() 
    keys = bit_combination(8)
    
    for encrypted_strings in encrypted_lines:
        hex_to_byte = codec_conversion(encrypted_strings)
        xor_cipher(hex_to_byte, keys)   
        

if __name__ == "__main__":
    single_char_xor()
