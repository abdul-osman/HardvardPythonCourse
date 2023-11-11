def main():
    x = int(input('x? '))
    if oddoreven(x):
        print('Even')
        oddorevensimplified(x)
    else:
        print('Odd')

    if oddorevensimplified(x):
        print('Even')
    else:
        print('Odd')

    if oddorevensimplifiedMORE(x):
        print('Even')
    else:
        print('Odd')


def oddoreven(y):
    if y % 2 == 0:
        return True
    else:
        return False


def oddorevensimplified(y):
    return True if y % 2 == 0 else False


def oddorevensimplifiedMORE(y):
    return y % 2 == 0


main()

