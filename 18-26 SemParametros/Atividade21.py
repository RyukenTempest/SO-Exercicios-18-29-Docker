n1: float = 0
n2: float = 0
n3: float = 0
n4: float = 0

def situacao():
    global n1, n2, n3, n4

    m = (n1 + n2 + n3 + n4) / 4

    print("Média:", m)

    if m >= 6:
        print("APROVADO")
    elif m >= 3:
        print("EXAME")
    else:
        print("RETIDO")


def main():
    global n1, n2, n3, n4

    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))

    situacao()


if __name__ == "__main__":
    main()