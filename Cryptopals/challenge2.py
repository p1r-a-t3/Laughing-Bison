def hex_to_decimal(args: str):
    return int(args, base=16)


def fixed_xor(args1: str, args2: str):
    import codecs
    # decode_string_1 = codecs.encode(
    #     codecs.decode(args1, 'hex'), 'base64').decode()
    
    decode_string_1 = ""
    for i in args1:
        _ = hex_to_decimal(i)
        decode_string_1 += str(_)
        
    decode_string_2 = ""
    for i in args2:
        _ = hex_to_decimal(i)
        decode_string_2 += str(_)
        
    # decode will make them string from byt3
    final_string = ""
    for i in range(0, len(decode_string_2)):
        string_1 = ord(decode_string_1[i])
        string_2 = ord(decode_string_2[i])

        xor = string_1 ^ string_2
        final_string += str(int(str(xor), base=16))

    print(final_string)


if __name__ == "__main__":
    fixed_xor("1c0111001f010100061a024b53535009181c",
              "686974207468652062756c6c277320657965")
