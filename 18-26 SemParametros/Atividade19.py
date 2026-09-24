n1: float = 0
n2: float = 0

def maior():
    global n1, n2

    if n1 > n2:
        print("Maior:", n1)
    else:
        print("Maior:", n2)


def main():
    global n1, n2

    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))

    maior()


if __name__ == "__main__":
    main()