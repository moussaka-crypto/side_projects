class Car:
    def __init__(self, brand, top_speed, autonomous=False):
        self.brand = brand
        self.top_speed = top_speed
        self.autonomous = autonomous

    def print_top_speed(self):
        print(f"{self.brand} has a top speed of {self.top_speed} kph.")

    # when both cars are autonomous -> accident
    def predict_accident(self, other):
        return self.autonomous and other.autonomous
    
if __name__ == "__main__":
    car1 = Car("BMW", 260, True)
    car2 = Car("Mercedes", 250, True)
    car3 = Car("Ford", 180, False)

    cars = [car1, car2, car3]
    for car in cars:
        car.print_top_speed()
    print()
    for i in range(len(cars)):
        for j in range(i, len(cars)):
            if cars[i].predict_accident(cars[j]):
                print(f"{cars[i].brand} and {cars[j].brand} will have an accident")
