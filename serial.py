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
    def __init__(self,start):
        self.start = start
        self.og = start
        
    def generate(self):
        print(self.start)
        self.start += 1
    
    def reset(self):
        self.start = self.og

    
        

serial = SerialGenerator(start=100)

serial.generate()
serial.generate()
serial.generate()
serial.reset()
serial.generate()
serial.generate()
