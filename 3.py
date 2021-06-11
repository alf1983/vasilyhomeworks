class ListMembersEx(Exception):
    def __init__(self, txt):
        self.txt = txt


result = []
input_member = ""
# input_member = input("Введите очередной член списка (только числа): ")
# if input_member.lower() == "stop":
#     print(f"Вы остановили программу на первом этапе. Резултат пустой список.")
while input_member.lower() != "stop":
    input_member = input("Введите член списка (только числа): ")
    if input_member != "stop":
        try:
            if input_member.isdigit() is False:
                raise ListMembersEx("Договорились же! Только числа, в список не вносим")
            else:
                check_member = int(input_member)
        except ValueError:
            pass
        except ListMembersEx as error:
            print(error)
        else:
            result.append(check_member)
print(result)
