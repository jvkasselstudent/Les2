def square_sum(numbers):
    total = 0
    for number in numbers:
        if number >= 0:
            total += number * number
    return total

test = square_sum([4,5,3,-81])

print(test)