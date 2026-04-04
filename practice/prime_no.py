# n=int(input("Enter a number: "))
# def print_prime(n):
#     if n<=1:
#         print("Not a prime number")
#     else:
#         for i in range(2,int(n**0.5)+1):
#             if n%i==0:
#                 print("Not a prime number")
#                 break
#         else:
#             print("Prime number")

# print_prime(n)



#PRINT ALL PRIME NUMBERS IN A GIVEN RANGE

def print_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

primes = print_primes_in_range(start, end)
print("Prime numbers:", primes)

print("Sum:", sum(primes))