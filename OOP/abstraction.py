class Car:
    def __init__(self, name, model, color, price):
        self.name = name
        self.model = model
        self.color = color
        self.price = price
        self.signal = None
        self.started = False
        self.moving = False

    def set_signal(self, signal):
        self.signal = signal.lower()

    def engine(self):
        if self.signal == "orange":
            print(f"{self.name} {self.model} engine is starting.")
            self.started = True
            self.moving = False

        elif self.signal == "green":
            if self.started:
                print(f"After a few tries, {self.name} has finally started moving.")
                self.moving = True
            else:
                print(f"{self.name} can't move yet. Start the engine first!")

        elif self.signal == "red":
            if self.started and self.moving:
                print(f"The traffic signal turned red, and {self.name} obediently came to a stop.")
                self.moving = False
            elif self.started and not self.moving:
                print(f"{self.name} is not even moving yet. It's just idling.")
            else:
                print(f"{self.name} isn't moving yet. Engine hasn't started.")

        else:
            print(f"Unknown or missing signal '{self.signal}'. {self.name} is waiting for a valid signal.")

    def stop(self):
        if self.moving:
            print(f"{self.name} has reached its destination and is now turned off.")
            self.moving = False
            self.started = False
        elif self.started and not self.moving:
            print(f"{self.name} didn't move at all. Turning off the idle engine.")
            self.started = False
        else:
            print(f"{self.name} is already off.")



bmw = Car("BMW", "M5", "Black", 62000000)
toyota = Car("Toyota", "Yaris", "gray", 7500000)
suzuki = Car("Suzuki", "Swift", "Black", 8200000)
jaguar = Car("Jaguar", "XF", "yellow", 87000000)


bmw.set_signal("orange")
bmw.engine()

bmw.set_signal("green")
bmw.engine()

bmw.set_signal("red")
bmw.engine()

toyota.set_signal("orange")
toyota.engine()

toyota.set_signal("green")
toyota.engine()

toyota.set_signal("red")
toyota.engine()
