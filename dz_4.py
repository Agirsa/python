workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for idx in range(len(workers)):
    name = workers[idx].split(' ')
    print("Привет, ", name[-1].capitalize(), "!", sep="")
