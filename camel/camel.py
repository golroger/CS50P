x = input(" camel case name :")
snake = ""
for i in x :
    if i.islower() :
        snake = snake + i
    if  i.isupper() :
        snake = snake + "_" + i.lower()

print( snake )

