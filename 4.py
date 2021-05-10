list_of_workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                   'директор аэлита']
for worker in list_of_workers:
    workers_parts = worker.split(" ")
    name = workers_parts[-1]
    print('Привет', name.title() + "!")
index = 1
while index < len(list_of_workers):
    workers_parts = list_of_workers[index].split(" ")
    workers_parts[-1] = workers_parts[-1].title()
    list_of_workers[index] = " ".join(workers_parts)
    index += 1
print(list_of_workers)
