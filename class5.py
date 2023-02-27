#to print fibonacci
from functools import lru_cache

@lru_cache
def fib( n):
    if n<=1:
        res= n
    else:
        res= fib(n-1)+fib(n-2)
        print(res)
        return res
n=int(input("Enter n terms: "))


