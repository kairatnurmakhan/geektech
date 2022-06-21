from get_car_info import CarInfo


class Car(CarInfo):
    def __init__(self, title, model, max_speed, color):
        CarInfo.__init__(self,title,model,max_speed,color)
        self.title = title
        self.model = model
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f"Output {self.title} {self.model} engine started")

    def stop_engine(self):
        print(f"Output {self.title} {self.model} engine stoped")


