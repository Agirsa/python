temperature = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
idx = 0
while idx < len(temperature):
    # вспомогательная переменная для упрощения чтения кода
    number = temperature[idx]
    if number.isdigit():
        temperature[idx] = f'"{int(temperature[idx]):02d}"'
    elif (number[0] == "+" or number[0] == "-") and int(number[1::].isdigit()):
        temperature[idx] = f'"{temperature[idx][0]}{int(temperature[idx][1::]):02d}"'
    idx += 1
string = ' '.join(temperature)
print(string)
