# For DEMO purposes only
# multiple statements per line is not well format.
#
# By Robert Schrijvers


# tuples are immutable lists

# definition
var_list = [1,3,6,4];           print('var_list = ',var_list, ' of type ',type(var_list))

var_tuple = (1,3,6,4);          print('var_tuple = ',var_tuple, ' of type ',type(var_tuple))



#Index for both
print('\nvar_list[1] = {0}  and  var_tuple[1] = {1}'.format(var_list[1],var_tuple[1] ) )









# Functions on both
print('\nlen(var_list) = {0} len(var_tuple) = {1}'.format(len(var_list),len(var_tuple) ) )
print('min(var_list) = {0} min(var_tuple) = {1}'.format(min(var_list),min(var_tuple) ) )
print('max(var_list) = {0} max(var_tuple) = {1}'.format(max(var_list),max(var_tuple) ) )



# methods on both
# count(argument)
print('\nvar_list.count(6) = {0} var_tuple.count(6) = {1}'.format(var_list.count(6),var_tuple.count(6)) )
# index(argument)
print('var_list.index(6) = {0} var_tuple.index(6) = {1}'.format(var_list.index(6),var_tuple.index(6)) )



#methods on list only
print('\nvar_list: ',var_list)

var_list.append(5) ;       print('var_list.append(5): ',var_list)
var_list.sort() ;          print('var_list.sort(): ',var_list)
var_list.reverse() ;       print('var_list.reverse(): ',var_list)
var_list.clear() ;         print('var_list.clear(): ',var_list)









# Conversion
var_list2 = list(var_tuple)
print('\nvar_list2 = ',var_list2, ' of type ',type(var_list2))

var_tuple2 = tuple(var_list2)
print('var_tuple2 = ',var_tuple2, ' of type ',type(var_tuple2))






