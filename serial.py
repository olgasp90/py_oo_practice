"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """initialize the generator, saving the start number for the reset function"""
        self.start = self.next = start

    def generate(self):
        """Return next episode"""
        self.start += 1
        return self.start - 1


    def restart(self):
        """Reset number"""
        self.start = self.next