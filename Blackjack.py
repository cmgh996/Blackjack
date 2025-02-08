import random

mazo = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

def calcular_valor(mano):
    valor_carta = sum([mazo[carta] for carta in mano])

    if valor_carta > 21 and "A" in mano:
        valor_carta -= 10
    return valor_carta


def mostrar_mano(jugador, mano):
    print(f"Mano del {jugador}: ", ", ".join(mano))

def dar_carta():
    carta = random.choice(list(mazo.keys()))
    return carta

def jugar_blackjack():

    mano_jugador = [dar_carta(), dar_carta()]
    mano_dealer = [dar_carta(), dar_carta()]


    mostrar_mano("Jugador", mano_jugador)
    print("Mano del dealer: ", mano_dealer[0], "y [Hidden]")

    while calcular_valor(mano_jugador) < 21:
        accion = input("Quieres (H)it o (S)tand? ").lower()
        if accion == 'h':
            mano_jugador.append(dar_carta())
            mostrar_mano("Player", mano_jugador)
        elif accion == 's':
            break
        else:
            print("Accion invalida! Usa 'h' para otra carta, o 's' para quedarte con tus cartas.")

    if calcular_valor(mano_jugador) > 21:
        print("Cagaste Batman! Te pasaste de lanza.")
        return

    print("\nTurno del dealer.")
    mostrar_mano("Dealer", mano_dealer)
    while calcular_valor(mano_dealer) < 17:
        print("Dealer saca una carta.")
        mano_dealer.append(dar_carta())
        mostrar_mano("Dealer", mano_dealer)

    if calcular_valor(mano_dealer) > 21:
        print("El dealer es pendejo. Ganaste!")
        return

    total_jugador = calcular_valor(mano_jugador)
    total_dealer = calcular_valor(mano_dealer)

    print(f"\nTu mano final: {mano_jugador} ({total_jugador})")
    print(f"La mano final del dealer: {mano_dealer} ({total_dealer})")

    if total_jugador > total_dealer:
        print("FATALITY!")
    elif total_jugador < total_dealer:
        print("QUE PENDEJO JAJAJAJAJA!")
    else:
        print("EMPATE. SE BESAN O QUE?")

if __name__ == "__main__":
    jugar_blackjack()