# For DEMO purposes only
# multiple statements per line is not well format.
#
# By Robert Schrijvers


# All data are objects, value determines type

print('\n---------------- All data are objects, value determines type -------------------')

# a boolean type
var = True;           print('var = ',var, ' of type ',type(var))

# an integer type
var = 5;              print('var = ',var, ' of type ',type(var))

# A float type
var = 5.0;            print('var = ',var, ' of type ',type(var))

# A string type
var = '5.0';          print('var = ',var, ' of type ',type(var))














print('\n---------------- Implicit conversion -------------------')
var1 = True
var2 = 5
var3 = var1 + var2
var4 = var3 + 8.2

print('var1 = ',var1, ' of type ',type(var1))
print('var2 = ',var2, ' of type ',type(var2))
print('var3 = ',var3, ' of type ',type(var3))
print('var4 = ',var4, ' of type ',type(var4))














# Objects are define by classes and have a "Constructors"
print('\n---------------- Explicit conversion -------------------')
var01 = int();          print('var01 = ',var01, ' of type ',type(var01))
var01 = int(True);      print('var01 = ',var01, ' of type ',type(var01))
var01 = int(5);         print('var01 = ',var01, ' of type ',type(var01))
var01 = int(5.6);       print('var01 = ',var01, ' of type ',type(var01))

var01 = float();        print('var01 = ',var01, ' of type ',type(var01))
var01 = float(True);    print('var01 = ',var01, ' of type ',type(var01))
var01 = float(5);       print('var01 = ',var01, ' of type ',type(var01))
var01 = float(5.2);     print('var01 = ',var01, ' of type ',type(var01))

var01 = str();          print('var01 = ',var01, ' of type ',type(var01))
var01 = str(True);      print('var01 = ',var01, ' of type ',type(var01))
var01 = str(5);         print('var01 = ',var01, ' of type ',type(var01))
var01 = str(5.2);       print('var01 = ',var01, ' of type ',type(var01))





