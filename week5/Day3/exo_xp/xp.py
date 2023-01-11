class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    def __str__(self):
        return f"{self.amount} {self.currency}"
    def __int__(self):
        return self.amount
    def __repr__(self):
        return f"{self.amount} {self.currency}"
    def __add__(self,other):
        try:
            return self.amount + other
        except:
            if self.currency==other.currency:
                return self.amount + other.amount
            elif self.currency!=other.currency:
                return f'TypeError: Cannot add between Currency type {self.currency} and {other.currency}'
    

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
print(str(c1))
print(int(c1))
print(repr(c1))
print(c1+5)
print(c1+c2)
print(c2)
print(c1+c3)
