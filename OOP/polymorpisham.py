from abc import ABC, abstractmethod

class Family(ABC):
    def __init__(self, name:str, age:int, color:str):
        self.name = name
        self.age = age
        self.color = color
    @abstractmethod
    def playingGame():
        pass

class Father(Family):
    def playingGame(self):
        print(f"{self.name} is playing Grand Theift Auto series")

class Mother(Family):
    def playingGame(self):
        print(f"{self.name} is playing Cooking Game")

class Son(Father):
    def watch(self):
        print("he is watching wwe")

class Daughter(Mother):
    def drink(self):
        print("she is drinking milk")

father = Father("Umair",32,"dusky")
mother = Mother("Nimra",28,"fair")
daughter = Daughter("Zainab",1,"wheatish")
son = Son("Bilal",4,"dusky")

daughter.playingGame()
son.playingGame()