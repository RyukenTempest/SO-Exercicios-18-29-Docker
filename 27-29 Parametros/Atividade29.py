def investimento(tipo, valor):
    if tipo == 1:
        valor = valor * 1.03
        print("Valor corrigido:", valor)
    elif tipo == 2:
        valor = valor * 1.05
        print("Valor corrigido:", valor)


def main():
    tipo = int(input("Tipo de investimento: "))
    valor = float(input("Valor investido: "))

    investimento(tipo, valor)


if __name__ == "__main__":
    main()