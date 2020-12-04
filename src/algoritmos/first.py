import random

def random_list():
    list = []
    for i in range(10):
        list.append(random.randrange(100))
    return list


'''' 
T(n) = c1n + c2(n-1)+c4(n-1)+c5SUM[n, j=2, tj]+c6SUM[n, j=2, tj - 1]+c7SUM[n, j=2, tj - 1]+c8(n-1) 
'''
def insertion_sort(list):
    for j in range(1, len(list)):           # custo c1 n
        chave = list[j]                     # custo c2 n - 1
        # comentário                        # custo 0 n - 1
        i = j - 1                           # custo c4 n - 1
        while i >= 0 and list[i] > chave:   # custo c5 SUM[n, j=2, tj]
            list[i+1] = list[i]             # custo c6 SUM[n, j=2, tj - 1]
            i = i - 1                       # custo c7 SUM[n, j=2, tj - 1]
        list[i+1] = chave                   # custo c8 n - 1


def fib_rec(n):
    if n <= 1:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib(n):
    a = 0
    p = 1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(n):
            aux = p
            p = a + p
            a = aux
        return p

if __name__ == '__main__':
    lista = random_list()
    print(lista)
    print("===ordenada===")
    lista = list(lista)
    insertion_sort(lista)
    print(lista)

