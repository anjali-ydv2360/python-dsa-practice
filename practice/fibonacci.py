n=int(input("Enter a number: "))

# METHOD 1

def fib(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b

fib(n)

# METHOD 2

def fibb(n):
    if n <= 1:
        return n
    return fibb(n-1) + fibb(n-2)

for i in range(n):
    print(fibb(i), end=" ")

# METHOD 3

def fibonacci(n):
    arr = [0, 1]
    
    for i in range(2, n):
        arr.append(arr[i-1] + arr[i-2])
    
    return arr

print(fibonacci(n))