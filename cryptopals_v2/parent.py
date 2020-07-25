import codecs

class Parent:
    
    """
    for some reason I don't seem to import this class
    """
    
    def __init__(self, *args, **kwargs):
        pass
    
    
    def hex_conversion(self, hex: str):
        """
        Takes a hex, decodes it, returns it.
        """
        return codecs.decode(hex, "hex")
    
    def base64_conversion(self, input: str):
        """
        takes any input, convert it to base64
        """
        return codecs.encode(input, "base64").decode()