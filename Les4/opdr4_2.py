def custom_sum(number_list):
    total = 0
    for number in number_list:
        total += number
    return total


test1 = custom_sum([1, 5, 8, 2])
test2 = custom_sum([7, -2, 1.5, 0.5])

print(test1)
print(test2)
