class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_width(self, thickness=25, weigh_per_sm=5):
        area = self._length * self._width * thickness * weigh_per_sm
        return area


d = Road(100, 20)
print(d.asphalt_width(20))
