"""def fibo(n):  
    if n <= 1:  
        return n  
    else:  
        return(fibo(n-1) + fibo(n-2))    
nterms = int(input("How many terms? "))    
if nterms <= 0:  
    print("Enter a number: ")  
else:  
    print("Fibonacci sequence: ")
    for i in range(nterms):  
        print(fibo(i))
######################################################
def fibonacci(n):
# return a list of fibonacci numbers
    if n == 0:
        fibonacci_list = []
    elif n == 1:
        fibonacci_list = [0]
    elif n == 2:
        fibonacci_list = [0, 1]
    elif n > 2:
        fibonacci_list = [0, 1]
        for i in range(n-2):
            fibonacci_list += [0]
            fibonacci_list[-1] = fibonacci_list[-2] + fibonacci_list[-3]
        return fibonacci_list

