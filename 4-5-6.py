class OutOfStock(Exception):
    def __init__(self,txt):
        self.txt = txt


class OfficeEquipment:
    def __init__(self, brand, model, count=0):
        self.brand = brand
        self.model = model
        self.count = count

    def receipting(self, **params):
        try:
            count = int(params['count'])
        except ValueError:
            print("Количество должно быть численым")
            exit(0)
        else:
            self.count += count

    def transference(self, **params):
        try:
            count = int(params['count'])
        except ValueError:
            print("Количество должно быть численым")
            exit(0)
        else:
            if self.count < count:
                raise OutOfStock("Нет необходимого количества")
            else:
                self.count -= count


class Printer(OfficeEquipment):
    def __init__(self, brand, count, model, connection_type, multi_color):
        super().__init__(brand, count, model)
        self.connection_type = connection_type
        self.multi_color = multi_color


class CopyMachine(OfficeEquipment):
    def __init__(self, brand, count, multi_color, flor):
        super().__init__(brand, count)
        self.multi_color = multi_color
        self.flor = flor


class Scanner(OfficeEquipment):
    def __init__(self, brand, count, connection_type):
        super().__init__(brand, count)
        self.connection_type = connection_type

