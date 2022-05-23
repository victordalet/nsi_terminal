def insere(a, tab):
    l = list(tab)
    l.append(a)
    i = len(l)-2
    while a < l[i] and i >= 0:
        l[i+1] = l[i]
        l[i] = a
        i = i-1
    return l

def main():
    print(insere(3,[1,2,4,5]))
    print(insere(10,[1,2,7,12,14,25]))
    print(insere(1,[2,3,4]))

main()