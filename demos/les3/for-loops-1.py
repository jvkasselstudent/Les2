# loop statements
# Demo purposes, may not be well formatted for display reasons
#
# Robert Schrijvers


# Basic for loop
# list
test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print('\ntest_data: ', test_data)
for item in test_data:
    print (item, type(item))
    print('bla')

# tuple
test_data= (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

print('\ntest_data: ', test_data)
for item in test_data:
    print (item, type(item))

# string
test_data = '1234567890'
print('\ntest_data: ', test_data)
for item in test_data:
    print (item, type(item))

