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

    def bytes_xor(self, a: bytes, b: bytes):
        """
        takes two bytes, xor them, returns the byte
        """
        return bytes([_a ^ _b for _a, _b in zip(a, b)])

    def bytes_to_hex_conversion(self, byte_string: bytes):
        """
        takes bytes string, convert it to hex
        """
        return codecs.encode(byte_string, "hex").decode()


if __name__ == "__main__":
    """
    >> https://cryptopals.com/sets/1/challenges/2

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

    converted_text_one = parent.hex_conversion(first_string)
    converted_text_two = parent.hex_conversion(second_string)
    result_byte = parent.bytes_xor(converted_text_one, converted_text_two)
    result_hex = parent.bytes_to_hex_conversion(result_byte)

    assert result_hex == "746865206b696420646f6e277420706c6179"

    # decimal_text_one = parent.string_to_decimal_conversion(converted_text_one)
    # decimal_text_two = parent.string_to_decimal_conversion(converted_text_two)

    # print(decimal_text_one, decimal_text_two)

    # result_decimal = parent.calculate_xor(decimal_text_one, decimal_text_two)
    # print(result_decimal)

    # result_hex = parent.decimal_to_hex_conversion(result_decimal)
    # print(result_hex)

    # print("#$#%" * 10)
    # print("#$#%" * 10)
    # print("#$#%" * 10)
    # print("#$#%" * 10)

    # first_hex_convert = parent.hex_to_decimal_conversion(first_string)
    # second_hex_convert = parent.hex_to_decimal_conversion(second_string)
    # print(first_hex_convert)
    # print(second_hex_convert)
    # xor_result_in_decimal = parent.calculate_xor(
    #     first_hex_convert, second_hex_convert)
    # print("*&ˆ%" * 10)
    # print("*&ˆ%" * 10)
    # print(xor_result_in_decimal)
    # xor_result_in_hex = parent.decimal_to_hex_conversion(xor_result_in_decimal)
    # print("*&ˆ%" * 10)
    # print(xor_result_in_hex)
