def sum(a, b):
    if b > 0:
        return sum(a + 1, b - 1)
    return a

print(sum(5, 5))