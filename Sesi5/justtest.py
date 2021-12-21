class Data:

    def __init__(self, value):
        self.value = value
        
    # def __add__(self, other):
    #     return Data(self.value + other.value)
    def __add__(self, other):
        return Data(self.value + other.value)


a = Data(40)
b = Data(2)
c = a + b

print(c.value)