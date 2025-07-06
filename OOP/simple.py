class Person:
    def __init__(self, name:str, gender:str, father:str, mother:str, color:str, phone:int, email:str):
        self.name = name
        self.gender = gender
        self.father = father
        self.mother = mother
        self.color = color
        self.phone = phone
        self.email = email

umair = Person("Umair khan","Male","Qayyum khan","Tehzeen khan", "Dusky", 923152681328, "umairkhann520@gmail.com")
nimra = Person("Nimra chaudhary","Female","Afaque chaudhary","Shabana chaudhary", "Fair", 923482526558, "nimidoll125@gmail.com")
print(umair.mother)
print(nimra.mother)