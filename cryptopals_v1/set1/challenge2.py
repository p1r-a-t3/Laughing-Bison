def hex_to_decimal(args: str):
    return int(args, base=16)

def convert_to_hex(args: int):
    return hex(args)[2:]


def fixed_xor(args1: str, args2: str):
    decoded_stuff = ""
    for index in range(0, len(args1)):
        _ = hex_to_decimal(args1[index]) ^ hex_to_decimal(args2[index])
        decoded_stuff += convert_to_hex(_)
    
    print(decoded_stuff)

if __name__ == "__main__":
    fixed_xor("1c0111001f010100061a024b53535009181c",
              "686974207468652062756c6c277320657965")
