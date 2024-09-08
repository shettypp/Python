# STRING 
print("hello"[4])
print("hello"[0])
# SUBSCRIPT : pulling out a spicfic element from a perticular position
print("1"+"23")
#print(1+23)
#anything inside quotes is considered as strings

#INTEGER
print(1+23)
123,456,789
123_456_789
#we can use underscore as comma

# FLOAT
#ex: 3.1453

#BOOLEAN
# TRUE or FALSE

#TypeCasting
#len(123)...Gives error..blz integer dont have any length
#num_char=len(input("what is ur name: ?"))
#print("your name has"+num_char+"characters")...this also gievs error
#In this case we have to convert integer to string but how???look down
num_char=len(input("what is your name?"))
new_num_char=str(num_char)
print("your name has "+new_num_char+" characters")

a=123
print(type(a))
a=str(123)
print(type(a))
a=float(123)
print(type(a))
