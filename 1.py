class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def number(cls, data):
        day, month, year = data.split("-")
        return int(day), int(month), int(year)

    @staticmethod
    def valid_data(data):
        data_int = Data(data)
        data_int = data_int.number(data)
        day_index = 0
        month_index = 1
        if 0 > data_int[month_index] or data_int[month_index] > 12:
            return f"Month in {data} is not valid"
        day_in_month = Data.check_day_count(data_int[month_index])
        if 0 > data_int[day_index] or data_int[day_index] > day_in_month:
            return f"Day in {data} is not valid"
        return f"Data {data} is valid"

    @staticmethod
    def check_day_count(month):
        count_31 = [1, 3, 5, 7, 8, 10, 12]
        if month in count_31:
            return 31
        elif month == 2:
            return 29
        return 30


data = Data("25-2-2019")
print(data.data)
print(data.number("25-2-2019"))
print(data.valid_data("31-2-2019"))
print(data.valid_data("30-12-2019"))
print(data.valid_data("30-15-2019"))