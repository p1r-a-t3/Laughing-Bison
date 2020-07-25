def hex_to_byte(hex: str):
    return (bytes.fromhex(hex)).decode('utf-8')


def convert_to_hex(args: int):
    return hex(args)[2:]


def repeating_xor(normal_text: str, key: str):
    encrypted_string = ""
    counter = 0
    for text in normal_text:
        __key = key[counter % len(key)]
        xor = ord(text) ^ ord(__key)
        encrypted_string += str(convert_to_hex(xor))
        print("text is {} when xored hex is is {}, xor is {}".format(
            text, str(convert_to_hex(xor)), xor))
        counter += 1

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Encrypted String:\n{}".format(encrypted_string))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return encrypted_string


# Previous decryption codes are based on single - key. They are not going to work.

if __name__ == "__main__":
    text1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    result = repeating_xor(text1, "ICE")
    supposed_result = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    print("length of result: {} and length expected: {}".format(len(result), len(supposed_result)))
    
    
    # for i in range(0, len(result)):
    #     if i < len(supposed_result):
    #         if result[i] != supposed_result[i]:
    #             print("Index: {}, result: {}, supposed to be: {}".format(i, result[i], supposed_result[i]))
    #     else:
    #         print("Ran out of juice at {}.".format(i))
    #         break