#1. Recursion Product using repeated addition
def multiply(a,b):
    if b < 0:
        return -multiply(a,-b)
    if b == 0:
        return 0
    return a + multiply(a,b -1)

print(multiply(3,4))

#2. Recursive exponetnial without using ** operator

def power(base,exp):
    if exp == 0:
        return 1
    if exp < 0:
        return 1/ power(base, -exp)
    return base * power(base, exp -1)

print(power(4,5))

#3. Recursive countdown: print n down to 0

def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)

print(countdown(5))

#4 Recursive Countup
def countup(m):
    def _count(i):
        if i > m:
            return
        print(i)
        _count(i + 1)
    _count(0)

print(countup(3))

#5 Recursive string reversal using concatenation
def reverse_string(s):
    if s == "":
        return ""
    return s[-1] + reverse_string(s[:-1])
print(reverse_string("Dog"))

#6. Recursivve prime checks if returns true then its prime false otherwise
def is_prime(z, divisor=2):
    if z <=1:
        return False
    if divisor * divisor > z:
        return True
    if z % divisor == 0:
        return False
    return is_prime(z, divisor + 1)
print(is_prime(7,2))

#7 Recursive Fibonnacci
#fibonacci(q) returns the qth fibonacci number
def fibonacci(q):
    if q <0:
        raise ValueError("Fibonacci number is not defined for negative indices")
    if q == 0:
        return 0
    if q == 1:
        return 1
    return fibonacci(q - 1)+ fibonacci(q - 2)
print(fibonacci(2))


