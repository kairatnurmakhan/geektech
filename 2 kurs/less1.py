# class User:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
# jack = User("Jack", "Barbaro", 20)
# print(jack.last_name)

# class Car:
#     def __init__(self, title, model, color):
#         self.title = title
#         self.model = model
#         self.color = color
# subaru = Car("Impreza", "WRX", "blue")
# print(subaru.title, subaru.model, subaru.color)

class Car:
     c = 0
     def __init__(self, title, model, engine, max_speed, speed, current_speed):
         self.title = title
         self.model = model
         self.engine = engine
         self.max_speed = max_speed
         self.speed = speed
         self.current_speed = current_speed



     def start_engine(self):
        print(f"""
Title: {self.title} {self.model}
Engine: {self.engine}
Max Speed: {self.max_speed}
Current speed: {self.current_speed}
        """)
     def stop_engine(self):
        if self.current_speed + self.speed > self.max_speed:
            print("check")
        else:
            self.current_speed += self.speed
            print(f"Current speed = {self.current_speed}")


bmw = Cars("BMW", "F10", "V8", 320, 60, 0)
mercedes = Cars("Mercedes", "W221", )
mark.gas()
mark.gas()
mark.gas()
mark.gas()

