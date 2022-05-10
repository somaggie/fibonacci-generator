fibonacciList = []

def fibonacciGenerator(n):
    if len(fibonacciList) > 9:
        print (fibonacciList)
        return
    else:
        l = n - 2
        m = n - 1
        fibonacciList.append((l + m))
        fibonacciGenerator(n + 1)
        return
    
print(' welcome to the fibonacci generator! The generator will give back a list of 5 fibonacci numbers based on the number given')
n = int(input(' Enter a number for the fibonacci genorator!'))
fibonacciGenerator(n)
