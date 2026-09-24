n1: int = 0
n2: int = 0
n3: int = 0
n4: int = 0

def crescente():
    global n1, n2, n3, n4

    if n4 < n1:
        print(n4, n1, n2, n3)
    elif n4 < n2:
        print(n1, n4, n2, n3)
    elif n4 < n3:
        print(n1, n2, n4, n3)
    else:
        print(n1, n2, n3, n4)


def main():
    global n1, n2, n3, n4

    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    n3 = int(input("Digite o terceiro valor: "))
    n4 = int(input("Digite o quarto valor: "))

    crescente()


if __name__ == "__main__":
    main()