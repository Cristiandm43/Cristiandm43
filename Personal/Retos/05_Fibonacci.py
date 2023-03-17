def fibonacci():

    prev = 0
    next = 1

    for number in range (1, 51):
        print(f"el numero {number} de fibonacci es {prev}")
        fib = prev + next
        prev = next
        next = fib

fibonacci()