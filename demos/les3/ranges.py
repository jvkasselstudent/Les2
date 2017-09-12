# ranges statements
# Demo purposes, may noit be well formatted for display reasons
#
# Robert Schrijvers

r = range(5) # = range(0,5,1)
print('\nrange :',r)
for item in r:
    print(item)


r = range(2,5) # range (2,5,1)
print('\nrange :',r)
for item in r:
    print(item)


r = range(2,12,2)
print('\nrange :',r)
for item in r:
    print(item)









print('\npowers of',range(0,17,2) )
for n in range(0,17,2):
    print('{0}**2 is {1} en {0}**3 is {2}'.format(n,n**2,n**3))