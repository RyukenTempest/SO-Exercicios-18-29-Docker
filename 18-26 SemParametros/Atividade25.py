h1: int = 0
m1: int = 0
h2: int = 0
m2: int = 0

def duracao():
    global h1, m1, h2, m2

    ini = h1 * 60 + m1
    fim = h2 * 60 + m2

    if fim <= ini:
        fim = fim + 24 * 60

    d = fim - ini

    print("Duração:", d // 60, "hora(s) e", d % 60, "minuto(s)")


def main():
    global h1, m1, h2, m2

    h1 = int(input("Hora inicial: "))
    m1 = int(input("Minuto inicial: "))
    h2 = int(input("Hora final: "))
    m2 = int(input("Minuto final: "))

    duracao()


if __name__ == "__main__":
    main()