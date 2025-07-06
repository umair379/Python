class Family:
    def __init__(self, name:str, age:int, color:str):
        self.name = name
        self.age = age
        self.color = color

class Father(Family):
    def hobbies(self):
        print(f"{self.name} watch WWE")

class Mother(Family):
    def hobbies(self):
        print(f"{self.name} watch pakistani dramas")

class Son(Father):
    pass

class Daughter(Mother):
    pass

umair = Father("Umair", 49, "dusky")
nimra = Mother("Nimra", 44, "fair")
zainab = Daughter("Zainab", 11, "fair")
bilal = Son("Bilal", 18, "dusky")

print(umair.name)
print(nimra.name)
zainab.hobbies()
bilal.hobbies()