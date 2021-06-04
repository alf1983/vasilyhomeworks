import time


class TrafficLight:
    def __init__(self, *user_color):
        self.__color = user_color

    def running(self):
        if self.__color != ('red', 'yellow', 'green'):
            raise ValueError(f'wrong colors {self.__color} should be red, yellow, green')
        pauses = [7, 2, 9]
        index = 0
        for c_color in self.__color:
            print(c_color)
            time.sleep(pauses[index])
            index += 1


traffic_light_1 = TrafficLight('red', 'yellow', 'green')
traffic_light_2 = TrafficLight('yellow', 'red', 'green')
traffic_light_1.running()
traffic_light_2.running()
