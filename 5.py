class Stationery:
    def __init__(self, s_title):
        self.title = s_title

    def draw(self):
        print(f'Запуск зарисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Ручка зарисовывает')


class Pencil(Stationery):
    def draw(self):
        print(f'Зарисовка карандашом')


class Handle(Stationery):
    def draw(self):
        print(f'Маркером быстрее')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.title)
pen.draw()
print(pencil.title)
pencil.draw()
print(handle.title)
handle.draw()