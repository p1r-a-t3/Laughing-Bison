def hex_to_base64(args: str):
    import codecs
    decoded_fuck_in_byte = codecs.decode(args, 'hex')
    decoded_fuck_in_base64_also_in_byte = codecs.encode(
        decoded_fuck_in_byte, 'base64')
    print(decoded_fuck_in_base64_also_in_byte.decode())
    return decoded_fuck_in_base64_also_in_byte.decode()


if __name__ == "__main__":
    hex_to_base64(
        "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
