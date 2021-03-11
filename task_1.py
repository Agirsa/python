def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield num


for val in odd_nums(19):
    print(val)


