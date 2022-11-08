class Operator:
    def __init__(self, num1:int, num2:int) -> None:
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def substract(self, inverse: bool = False):
        if inverse:
            return self.num2 - self.num1
        return self.num1 - self.num2

    def substract2(self, inverse: bool = False):
        if inverse:
            return self.num2 - self.num1
        return self.num1 - self.num2

