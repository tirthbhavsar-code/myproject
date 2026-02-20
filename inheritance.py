class Father:
    def money(self):
        print("Father money")

class Son(Father):
    def bike(self):
        print("Son bike")

s = Son()
s.money()
s.bike()
