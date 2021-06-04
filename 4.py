class Car:
    def __init__(self, **kwargs):
        self.speed = kwargs['speed']
        self.color = kwargs['color']
        self.name = kwargs['name']
        self.is_police = kwargs['police']

    def go(self):
        print(f'{self.name} машина поехала')

    def stop(self):
        print(f'{self.name} машина Остановилась')

    def turn(self, direction):
        print(f'{self.name} машина повернула на ', direction)

    def show_speed(self):
        print(f'Скорость машины {self.speed}')


class TownCar(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_speed(self):
        if self.speed > 60:
            print(f"{self.speed} это привышение скорости")


class SportCar(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class WorkCar(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_speed(self):
        if self.speed >40:
            print(f'{self.speed} это превышение скорости')


class PoliceCar(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


town_car = TownCar(speed=71, color='silver', name='Toyota', police=False)
print(town_car.speed)
print(town_car.color)
print(town_car.name)
print(town_car.is_police)
print(town_car.go())
print(town_car.show_speed())
sport_car = SportCar(speed=150, color='red', name='BMW', police=False)
print(sport_car.speed)
print(sport_car.color)
print(sport_car.name)
print(sport_car.is_police)
print(sport_car.show_speed())
work_car = WorkCar(speed=42, color='white', name='Mercedes', police=False)
print(work_car.speed)
print(work_car.color)
print(work_car.name)
print(work_car.is_police)
print(work_car.show_speed())
police_car = PoliceCar(speed=50, color='blue', name='Skoda', police=True)
print(police_car.speed)
print(police_car.color)
print(police_car.name)
print(police_car.is_police)
print(police_car.show_speed())

