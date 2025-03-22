#Inverted right angled triangle
def pattern(n):
    for i in range(n):
        for j in range (i,n):
            print ("*", end="")
        print()

pattern (5)

#Right angled triangle
def pattern(n):
    for i in range(n):
        for j in range (i+1):
            print ("*", end="")
        print()

pattern (5)

#Diamond

def pattern(n):
    for i in range(n):
        for j in range (i,n):
            print (" ", end=" ")           
        for j in range (i):
            print ("*", end=" ")
        for j in range (i+1):
            print ("*", end=" ")
        
        print()

    for i in range(n - 2, -1, -1):  
        for j in range(n - i):  
            print(" ", end=" ")
        for j in range(2 * i + 1):  
            print("*", end=" ")

        print()
        
pattern (5)

#Pyramid

def pattern(n):
    for i in range(n):
        for j in range (i,n):
            print (" ", end="")
            
        for j in range (i):
            print ("*", end="")

        for j in range (i+1):
            print ("*", end="")
        
        print()

pattern(5)