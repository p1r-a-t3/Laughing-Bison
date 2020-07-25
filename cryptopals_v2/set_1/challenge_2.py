import codecs


class Parent:

    def __init__(self, *args, **kwargs):
        pass

    def hex_conversion(self, hex: str):
        """
        Takes a hex, decodes it, returns a bytes.
        """
        return codecs.decode(hex, "hex")

    def base64_conversion(self, input: str):
        """
        takes any input, convert it to base64,
        """
        # without decode, this function returns bytes
        return codecs.encode(input, "base64").decode()

    def string_to_binary_conversion(self, input: str):
        """ 
        Takes a string, returns the binary
        """
        return (int)(''.join(format(ord(i), 'b') for i in input))

    def calculate_xor(self, value_a: int, value_b: int):
        """ 
        takes two inputs as int and returns an int (decimal)
        """
        return value_a ^ value_b

    def hex_to_decimal_conversion(self, hex: str):
        """
        takes a hex, returns decimal int
        """
        return int(hex, 16)

    def decimal_to_binary_conversion(self, decimal: int):
        """
        takes a decimal integer, returns a binary integer/number
        """
        return bin(decimal)

    def hex_to_binary_conversion(self, hex: str):
        """
        takes a hex string, returns the binary integer/number
        """
        decimal = self.hex_to_decimal_conversion(hex)
        return self.decimal_to_binary_conversion(decimal)

    def decimal_to_hex_conversion(self, decimal: int):
        """
        takes a decimal integer value, returns its hex
        """
        return int(str(decimal), 16)


if __name__ == "__main__":
    """
    For this problem, hex to string is not needed
    XOR can be done between two numbers only. 
    I have converted the hex to decimals and then XORed them
    and the result is in decimal. So I convert the result in hex again. 
    It does not work.

    Need to write: a readme side by side with my thought process -- may be!
    Need to fix: parent function does not import
    """
    parent = Parent()
    first_string = "1c0111001f010100061a024b53535009181c"
    second_string = "686974207468652062756c6c277320657965"

    first_hex_convert = parent.hex_to_decimal_conversion(first_string)
    second_hex_convert = parent.hex_to_decimal_conversion(second_string)

    print(first_hex_convert)
    print(type(first_hex_convert))
    print(type(second_hex_convert))

    xor_result_in_decimal = parent.calculate_xor(
        first_hex_convert, second_hex_convert)
    print("*&ˆ%" * 10)
    print("*&ˆ%" * 10)
    print(xor_result_in_decimal)
    xor_result_in_hex = parent.decimal_to_hex_conversion(xor_result_in_decimal)
    print("*&ˆ%" * 10)
    print(xor_result_in_hex)
