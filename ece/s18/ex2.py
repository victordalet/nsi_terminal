def inverse_chaine(chaine):
    result = ''
    for caractere in chaine:
        result = caractere + result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return chaine == inverse

def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)

def main():
    print(est_nbre_palindrome(213312))
    print(est_nbre_palindrome(214312))

main()