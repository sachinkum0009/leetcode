from typing import List
# def fib(n: int):
#     if n <= 1:
#         return 1
#     return fib(n-1) + fib(n-2)

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# def fibRec(n: int, memo: List):
#     if n <= 1:
#         return n
    
#     if memo[n] != -1:
#         return memo[n]
    
#     memo[n] = fibRec(n-1, memo) + fibRec(n-2, memo)
#     return memo[n]

# def fib(n: int):
#     memo = [-1]*(n+1)
#     return fibRec(n, memo)

if __name__ == '__main__':
    print(f" fib of 5: {fib(100)}")
    
