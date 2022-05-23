def binaire(a):
    bin_a = str(1)
    a = a // 2
    while a != 1 :
        bin_a = str(a%2) + bin_a
        a = a //2
    return bin_a

def main():
    print(binaire(77))

main()
