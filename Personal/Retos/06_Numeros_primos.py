def is_prime(number):
    if number < 2:
        return False

    for index in range (2, number):
        if number % index == 0:
            return False
    return True

for index in range(1,101):
    if is_prime(index):
        print(index)