n1: int = 0
n2: int = 0

def multiplo():
    global n1, n2

    if n1 > n2:
        ma = n1
        me = n2
    else:
        ma = n2
        me = n1

    if ma % me == 0:
        print("É múltiplo")
    else:
        print("Não é múltiplo")


def main():
    global n1, n2

    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))

    multiplo()


if __name__ == "__main__":
    main()