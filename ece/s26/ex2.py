def separe(tab):
    i = 0
    j = len(tab)-1
    while i < j :
        if tab[i] == 0 :
            i = i+1
        else :
            tab[i], tab[j] = tab[j],tab[i]
            j = j-1
    return tab


def main():
    print(separe([1, 0, 1, 0, 1, 0, 1, 0]))

main()