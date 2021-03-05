def num_translate(num):
    print(numbers.get(num))


numbers = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
           "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
number = input("Напишите число на английском: ")
num_translate(number)

