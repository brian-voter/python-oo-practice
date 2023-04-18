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
        self.start = start
        self.current_serial = self.start

    def reset(self):
        """Resets so that the next call to generate() returns the starting number"""
        self.current_serial = self.start

    def generate(self):
        """Generates a serial number one higher than the last one generated,
        starting from the start number specified"""
        next_serial = self.current_serial
        self.current_serial += 1
        return next_serial