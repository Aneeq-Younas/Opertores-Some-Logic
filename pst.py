def add (x, y):
    while y != 0:
        num = x & y
        x = x ^ y
        y = num << 1
    return x

print(add(15, -30))
print(add(5, 14))
print(add(12, -15))
print(add(6, 16))
print(add(-15, -2))