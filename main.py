import functools

# versão livro
def pos_sum(a, num_of_entries):
    sum = 0
    i = 1 # todo: pra gerar erro!
    while(i < num_of_entries):
        if(a[i] > 0):
            sum = sum + a[i]
        i = i + 1
    return sum

# versão recursiva
def pos_sum2(a):
    if len(a) == 1:
        return a[0]
    elif a == []:
        return 0
    else:
        a[1] = a[0] + a[1]
        list = a[1:]
        return pos_sum2(list)

# versão funcional -> not so good
def pos_sum3(seq, initial = 0):
  return functools.reduce(lambda x, y: x + y, seq, initial)


if __name__ == '__main__':
    lista = [1,2,3,4]
    print("Tamanho da lista: ", len(lista))
    print("func1: ", pos_sum(lista, 4))
    print("func2: ", pos_sum2(lista))
    print("func3: ", pos_sum3([1,2,3,4], 0))