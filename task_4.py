src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


rezult = (val for i, val in enumerate(src) if src[i-1] < src[i] and i != 0)
print(type(rezult))
print(*rezult, sep=", ")