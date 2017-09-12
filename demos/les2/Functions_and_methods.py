# For DEMO purposes only
# multiple statements per line is not well format.
#
# By Robert Schrijvers



# Functions versus methods

var = [1,4,6,77,2,8,3]

# function
length = len(var)

# method: sort is defined for type list
var.sort()









# Python build in functions

# core functions, no import needed
len(var)
print('number of elements of var is ', len(var))

# eval, evaluates a string and executes it
result = eval('2**8')
print('result is' ,result)

# input: reads from standdard input
result = input('\nType your input: ')
print('your input was:',result)

# Combining functions
result = eval(input('\nType your expression: '))
print('The outcome is:',result)






# Additional function in bundled modules:
#dat ben ik
# import a module (all functions and classes from module)
import math

n = 12
wortel_n = math.sqrt(n)
print('\nWortel van {0} is {1} in kwadraat is weer {2}'.format(n,wortel_n,wortel_n**2))


# import a function from a module
from statistics import mean
from statistics import median

values = [2,3,4,5,6,7,1,9]
mean_value = mean(values);          print('Gemiddelde van {0} is {1}'.format(values,mean_value))
median_value = median(values);      print('Mediaan    van {0} is {1}'.format(values,median_value))







