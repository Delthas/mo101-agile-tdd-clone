class Binary:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    def __index__(self):
        return int(self.number, base=2)
        
    def __bin__(self):
        return bin(self.__index__())

    def __hex__(self):
        return hex(self.__index__())

    def __int__(self):
        return int(self.number, base=2)
        
    def __getitem__(self, key):
        return self.number[key]

    def fun_xor(bin1, bin2):
        return Binary(str(int(bin1) ^ int(bin2)))

    def fun_or(bin1, bin2):
        return Binary(str(int(bin1) | int(bin2)))
        
    def fun_and(bin1, bin2):
        return Binary(str(int(bin1) & int(bin2)))

    def __add__(self, other):
        return Binary('0')

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
	print(Binary.fun_xor(Binary('101'), Binary('001')))
