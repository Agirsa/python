# задание А
price = [57.8, 46.51, 97, 91.43, 80.0, 4, 8, 15, 16, 23, 42, 17.98, 11.00, 9]
for idx in range(len(price)-1):
    ruble = int(price[idx])
    penny = int(float(price[idx]) * 100 % 100)
    print(f'{ruble} руб {penny:02d} коп', end=", ")
idx += 1
ruble = int(price[idx])
penny = int(float(price[idx]) * 100 % 100)
print(f'{ruble} руб {penny:02d} коп')

# задание B
print(id(price))
price.sort()
for idx in range(len(price)-1):
    ruble = int(price[idx])
    penny = int(float(price[idx]) * 100 % 100)
    print(f'{ruble} руб {penny:02d} коп', end=", ")
idx += 1
ruble = int(price[idx])
penny = int(float(price[idx]) * 100 % 100)
print(f'{ruble} руб {penny:02d} коп')
print(id(price))

# задание С
new_price = sorted(price, reverse=True)
for idx in range(len(new_price)):
    ruble = int(new_price[idx])
    penny = int(float(new_price[idx]) * 100 % 100)
    new_price[idx] = f'{ruble} руб {penny:02d} коп'
print(' '.join(new_price))

# задание D
print(' '.join(new_price[:5:]))





