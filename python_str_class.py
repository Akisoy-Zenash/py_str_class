class Str():
    def __init__(self, inpput):
        self.inpput = inpput
    def covert(self):
        print(f"{self.inpput}")
    

test_01 = Str(5)
test_01.covert()
print(type(test_01.covert()))