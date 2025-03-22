#*args -> Allows the function to accept any number of arguments
#      -> Stored as tuple   

def add(*args):
    return sum(args)  
     
print(add(5, 10, 15, 20))

#**kwargs -> Allows the function to accept any number of arguments
#      -> Stored as dictionary   

def person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person(name="Jude", age=24, city="Bengaluru")
