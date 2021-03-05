def num_translate(num):
    if num[0].isupper():
        print(numbers.get(num.lower()).capitalize())
    else:
        print(numbers.get(num))


numbers = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
           "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
number = input("Напишите число на английском: ")
num_translate(number)

