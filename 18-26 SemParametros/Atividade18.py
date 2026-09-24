n1: int = 0
n2: int = 0

def diferenca():
    global n1, n2

    if n1 > n2:
        d = n1 - n2
    else:
        d = n2 - n1

    print("A diferença é:", d)


def main():
    global n1, n2

    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))

    diferenca()


if __name__ == "__main__":
    main()