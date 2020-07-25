def fib(arg):
    if arg <= 0:
        print('wrong')
    elif arg == 1 or arg == 2:
        return 1
    else:
        return fib(arg-1) + fib(arg-2)
    
