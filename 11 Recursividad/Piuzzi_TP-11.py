# import sys

# sys.setrecursionlimit(2000)

# def factorial_recur(x):
#     return 1 if x == 0 else x * factorial_recur(x-1)
#     # if x == 0:
#     #     return 1
#     # else:
#     #     return x * factorial_recur(x-1)
    
# print(factorial_recur(5))

def repetir_frase(num,frase):
    if num >= 1:
        print(frase)
        repetir_frase(num-1, frase)

repetir_frase(3, "hola")

