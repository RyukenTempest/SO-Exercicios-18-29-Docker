def velocidade(voltas, ext, tempo):
    d = voltas * ext
    v = (d / 1000) / (tempo / 60)

    print("Velocidade média:", v, "km/h")


def main():
    voltas = int(input("Número de voltas: "))
    ext = float(input("Extensão do circuito em metros: "))
    tempo = float(input("Tempo em minutos: "))

    velocidade(voltas, ext, tempo)


if __name__ == "__main__":
    main()