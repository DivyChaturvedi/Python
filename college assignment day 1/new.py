'''Recursion'''
# def rec(n):
#     if n>10:
#         return 0
#     else:
#         print(n)
#     return rec(n+1)

# rec(1)

'''fibonaccoi using recursion'''

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input())
for i in range(n):
    print(fibo(i),end=" ")        
            




        

