def factorial(n):
    if n < 0:
        return "undefined"
    if n <= 1:
        return 1
    return n*factorial(n-1)

def summation(n):
    if n <= 0:
        return 0
    return n + summation(n-1)

def exponential(base, power):
    if power < 0:
        return 'Negative powers not supported'
    if power == 0:
        return 1
    return base * exponential(base, power - 1)

def fibonacci(n):
    if n < 0:
        return 'undefined'   	
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2) 

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

def product(n):
    if n == 0:
        return 1
    return (n % 10) * product(n // 10)

def product_two(a, b):
    if b == 0:
        return 0
    return a + product_two(a, b - 1)

def sum_of_range(start, end):
    if start > end:
        return 0
    return start + sum_of_range(start + 1, end)

def reverse(n, reversed_n=0):
    if n == 0:
        return reversed_n
    return reverse(n // 10, reversed_n * 10 + n % 10)

def Euclid(a, b):
    if b == 0:
        return a
    return Euclid(b, a % b)

def interest(p, r, t):
    if t == 0:
        return p
    return interest(p * (1 + r), r,  t -1)

def combinations(n, r):
    if r == 0 or r == n:
        return 1
    return combinations(n-1, r-1) + combinations(n-1, r)

def main():
    while True:
        print("1. Factorial of a number")
        print("2. Summation of a number")
        print("3. Power/exponential function")
        print("4. Fibonacci’s numbers")
        print("5. Sum of a number’s digits")
        print("6. Product of number’s digits")
        print("7. Product of two whole numbers")
        print("8. Sum of numbers in a range")
        print("9. Reverse the digits in a number")
        print("10. Euclid’s GCD algorithm")
        print("11. Find a compound interest balance")
        print("12. Find combinations of item")
        print("13. Exit")
        print("\n")

        choice = int(input("Enter choice 1-13: ")) 
            
        if choice == 1:
            number = int(input("Enter a number: "))
            print(f"The result of the function is: {factorial(number)} \n ")

        elif choice == 2:
            number = int(input("Enter a number: "))
            print(f"The result of the function is: {summation(number)} \n ")

        elif choice == 3:
            base = int(input("Enter a base: "))
            power = int(input("Enter a power: "))
            print(f"The result of the function is: {exponential(base, power)} \n ")

        elif choice == 4:
            number = int(input("Enter a number: "))
            print(f"The result of the function is: {fibonacci(number)} \n ")

        elif choice == 5:
            number = int(input("Enter a number: "))
            print(f"The result of the function is: {sum_digits(number)} \n ")

        elif choice == 6:
            number = int(input("Enter a number: "))
            print(f"The result of the function is: {product(number)} \n ")

        elif choice == 7:
            a = int(input("Enter number a: "))
            b = int(input("Enter number b: "))
            print(f"The result of the function is: {product_two(a, b)} \n ")
  
        elif choice == 8:
            start = int(input("Enter a start number: "))
            end = int(input("Enter a end number: "))
            print(f"The result of the function is: {sum_of_range(start, end)} \n ")

        elif choice == 9:
            number = int(input("Enter a number: "))
            print(f"The result of the function is: {reverse(number)} \n ")

        elif choice == 10:
            a = int(input("Enter number a: "))
            b = int(input("Enter number b: "))
            print(f"The result of the function is: {Euclid(a, b)} \n ")
 
        elif choice == 11:
            p = int(input("Enter principal: "))
            r = float(input("Enter rate as decimal: "))
            t = int(input("Enter time: "))
            print(f"The result of the function is: {interest(p, r, t)} \n ")
  
        elif choice == 12:
            a = int(input("Enter a number: "))
            b = int(input("Enter a number: "))
            print(f"The result of the function is: {combinations(a, b)} \n ")

        elif choice == 13:
        	break
main()

