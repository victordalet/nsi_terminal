def main():
    a = [i for i in range(10)]
    for i in a :
        match i:
            case 2:
                print('yo')
            case 5 :
                print('midlle')
                
main()