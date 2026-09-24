n1: int = 0
n2: int = 0

def crescente():
    global n1, n2

    if n1 < n2:
        print(n1, n2)
    else:
        print(n2, n1)


def main():
    global n1, n2

    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))

    crescente()


if __name__ == "__main__":
    main()