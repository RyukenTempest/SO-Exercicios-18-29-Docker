import math

a: float = 0
b: float = 0
c: float = 0

def equacao():
    global a, b, c

    if a == 0:
        print("Não é uma equação de 2º grau.")
    else:
        d = b ** 2 - 4 * a * c

        if d < 0:
            print("Não existem raízes reais.")
        else:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)

            print("X1:", x1)
            print("X2:", x2)


def main():
    global a, b, c

    a = float(input("Digite A: "))
    b = float(input("Digite B: "))
    c = float(input("Digite C: "))

    equacao()


if __name__ == "__main__":
    main()