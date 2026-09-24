n: int = 0

def divisivel():
    global n

    if n % 2 == 0 and n % 3 == 0:
        print("É divisível por 2 e 3.")
    else:
        print("Não é divisível por 2 e 3.")


def main():
    global n

    n = int(input("Digite um número: "))

    divisivel()


if __name__ == "__main__":
    main()