ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    resultat = ''
    for lettre in message :
        if lettre in ALPHABET :
            indice = (position_alphabet(lettre)+decalage)%26
            resultat = str(resultat) + str(ALPHABET[indice])
        else:
            resultat = resultat + ' '
    return resultat

def main():
    print( cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !',-5))

main()