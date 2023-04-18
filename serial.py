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

    def __init__(self, start):
        """Creates a new SerialGenerator with the given starting number"""
        self.start = self.current_serial = start

    def reset(self):
        """Resets so that the next call to generate() returns the starting number"""
        self.current_serial = self.start

    def generate(self):
        """Generates a serial number one higher than the last one generated,
        starting from the start number specified"""
        self.current_serial += 1
        return self.current_serial - 1