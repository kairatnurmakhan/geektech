

class CarInfo():
    def __init__(self, title, model, max_speed, color):

        self.title = title
        self.model = model
        self.max_speed = max_speed
        self.color = color


    def car_info(self):
        print(f"""
        Title: {self.title}
        Model: {self.model}
        Max_speed: {self.max_speed}
        Color: {self.color} """)




