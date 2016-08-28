from array import *

def fib_lin(n):
    return fib_iter (1, 0, n)
def fib_iter(a, b, counter):
    if counter <= 0:
        return b
    else:
        return fib_iter ((a + b), a, (counter - 1))
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib2(n):
    if n == 0:
        return 0
    a = 1
    b = 0
    for i in range(1,n):
        a,b = (a+b),a        
    return a
        


coins = [1,7,15]



def opweg(n):
    coins = [1,7,15]
    optl = []
    for i in range(0, n+1):
        optl.append(i)
    arr = array('i', optl)
    for i in range (2,n+1):
        k = arr[i]
        for t in coins:
            if (k >= t):

                if arr[i] > (arr[i-t] + 1):
                    arr[i] = arr[i-t] + 1
                    

    return arr[n]



def restaurant(n):
    products = [("Mixed Fruit",215),("French Fries", 275),
             ("Side Salad", 335),("Hot Wings", 355),
                ("Mozzarella Sticks",420),("Sampler Plate",580)]
    optl = []
    for i in range(0, n+1):
        optl.append([])
        

    for i in range (0,n+1):
        for t in products:
            if i-t[1] >= 0:
                optl[i] = optl[i-t[1]]
                optl[i].insert(0, t[0])
            
            
    return optl[n]
