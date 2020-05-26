import functools

# versão livro todo: identificar falhas
def pos_sum(a, num_of_entries):
    sum = 0
    i = 0 # todo: pra gerar erro!
    while(i < num_of_entries):
        if(a[i] > 0):
            sum = sum + a[i]
        i = i + 1
    return sum

# versão melhorada
def pos_sum1(a):
    sum = 0
    for i in a:
        sum += i
    return sum

# versão recursiva
def pos_sum2(a):
    if len(a) >  1:
        head, *tail = a
        tail[0] = tail[0] + head
        return pos_sum2(tail)
    elif a == []:
        return 0
    else:
        return a[0]

# versão funcional -> not so good
def pos_sum3(seq, initial = 0):
  return functools.reduce(lambda x, y: x + y, seq, initial)


if __name__ == '__main__':
    lista = [1,2,3,4]
    print("Tamanho da lista: ", len(lista))
    print("func1: ", pos_sum(lista, 4))
    print("func2: ", pos_sum2(lista.copy()))
    print("func3: ", pos_sum3(lista, 0))
    print("func4: ", pos_sum1(lista))