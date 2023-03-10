def exponentiation(base, degree):
    if degree > 0:
        return base * exponentiation(base, degree - 1)
    return 1

print(exponentiation(5, 0))