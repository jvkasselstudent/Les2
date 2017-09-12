# if statements
# Demo purposes, may noit be well formatted for display reasons
#
# Robert Schrijvers

# one way decision
#

# input
jarig = True
leeftijd = 19



print('Jarig: ',jarig)
print('Leeftijd: ', leeftijd)





print ('\n\n ------------- 1 way decision ----------------')

print ('Hallo')
if jarig:
    print('Stukje taart?')
    print('Gefelicteerd')
print('Frisje?')






print ('\n\n ------------- 1 way decision ----------------')
print ('Hallo')
if jarig and leeftijd >= 18 :
    print ('Biertje?')
    print('Stukje taart?')
print('Frisje?')







print ('\n\n ------------- 2 way decision ----------------')
print ('Hallo')

if leeftijd >= 18 :
    print ('Biertje?')
else:
    print('Frisje?')









print ('\n\n ------------- 2 way decision ----------------')
print ('Hallo')

if jarig and leeftijd >= 18 :
    print ('Biertje?')
    print('Stukje taart?')
else:
    print('Frisje?')










print ('\n\n ------------- multiple cases ----------------')
print ('Hallo')

if jarig and leeftijd >= 18 :
    print ('Biertje?')
    print('Stukje taart?')
if jarig and leeftijd < 18:
     print('Frisje?')
     print('Stukje taart?')
if not jarig and leeftijd < 18:
    print('Frisje?')
if not jarig and leeftijd >= 18:
    print('Biertje?')











print ('\n\n ------------- Nested decision ----------------')
print ('Hallo')
if jarig:
    print('Stukje taart?')
    if leeftijd >= 18:
        print('Gefeliciteerd, Biertje?')
    else:
        print('Gefeliciteerd, Frisje?')
else:
    if leeftijd >= 18:
        print('Biertje?')
    else:
        print('Frisje?')








print ('\n\n ------------- elif ----------------')
print ('Hallo')
if jarig:
    print('Stukje taart?')

if leeftijd > 40:
    print('Wijntje?')
elif leeftijd > 18:
    print('Biertje?')
elif leeftijd == 18:
    print('Je eerste Biertje?')
else:
    print('Frisje?')





