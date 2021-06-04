class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


a = Position('Dim', 'Verin', 'Director', {'wage': 10000, 'bonus': 5000})
print(a.name)
print(a.surname)
print(a.position)
print(a._income)
print(a.get_total_income())
print(a.get_full_name())
