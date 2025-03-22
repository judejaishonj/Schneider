#return
def add(a, b):
    return a + b  

result = add(5, 3)
print(result)

#yield
def count(n):
    for i in range(1, n + 1):
        yield i 

value = count(5)

for num in value:
    print(num)