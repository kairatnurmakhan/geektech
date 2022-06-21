class Transport:
    def __init__(self, title, engine, color, model, tachometer ):
        self.title = title
        self.engine = engine
        self.color = color
        self.model = model
        self.tachometer = tachometer


    def start_engine(self):
        print(f"On {self.title} {self.model} engine started")


    def stop_engine(self):
        print(f"On {self.title} {self.model} engine stoped")


    def car_check(self):
        if self.tachometer < 1:
            print("Check ON!")
        else:
            print("Check OFF!")


class Car(Transport):
    def __init__(self, title, engine, color, model, tachometer, max_speed):
        super().__init__(title, engine, color, model, tachometer)
        self.max_speed = max_speed


class Tesla(Car):
    pass

tesla = Car(
    "Tesla",
    "electra car",
    "black",
    "plaid",
    1,
    260
)

print(tesla.max_speed)
tesla.start_engine()
tesla.car_check()

