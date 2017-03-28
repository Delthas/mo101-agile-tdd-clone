class Binary:
    def __init__(self, number):
        self.number = number

    def __index__(self):
        return int(self.number, base=2)
        
    def __bin__(self):
        return '0b' + self.number

    def __hex__(self):
        return hex(self.__index__())

    def __int__(self):
        return int(self.number, base=2)
        
    def __getitem__(self, key):
        return self.number[key]

    def __add__(self, other):
        pass

class SizeBinary:
    def __init__(self, number, size):
        self.number = number
        self.size = size

if __name__ == "__main__":
	b = Binary('0101110001')
	print(b.__hex__())
	print(int(b))
	print(bin(b))
	print(b[9])
