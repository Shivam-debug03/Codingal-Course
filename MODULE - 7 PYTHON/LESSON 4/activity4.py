#Python program  to check if a number is prime
#Take input from the user
num = int(input("Enter a number : "))
#Check if number is greater than 1 (since primes are > 1)
if num > 1:
    for i in range (2 , int(num** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")