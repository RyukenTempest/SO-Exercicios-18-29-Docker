def preco(venda, p):
    if venda < 500 and p < 30:
        p = p * 1.10
    elif venda < 1000 and p < 80:
        p = p * 1.15
    elif venda >= 1000 and p >= 80:
        p = p * 0.95

    print("Novo preço:", p)


def main():
    venda = float(input("Média mensal de vendas: "))
    p = float(input("Preço atual: "))

    preco(venda, p)


if __name__ == "__main__":
    main()