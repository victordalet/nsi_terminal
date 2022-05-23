def tri(tab):
    i= 0
    j= len(tab)-1
    while i != j :
        if tab[i]== 0:
            i= i+1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j = j-1
    return tab

def main():
    print(tri([0,1,0,1,0,1,0,1,0]))

main()