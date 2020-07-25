import codecs


class Parent:

    def __init__(self, *args, **kwargs):
        pass

    def hex_conversion(self, hex: str):
        """
        Takes a hex, decodes it, returns it.
        """
        return codecs.decode(hex, "hex")

    def base64_conversion(self, input: str):
        """
        takes any input, convert it to base64,
        """
        # without decode, this function returns bytes
        return codecs.encode(input, "base64").decode()


if __name__ == "__main__":
    parent = Parent()
    hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

    human_readable_mushroom_text = parent.hex_conversion(hex_string)
    print(human_readable_mushroom_text)

    base64 = parent.base64_conversion(human_readable_mushroom_text)
    print(base64)
