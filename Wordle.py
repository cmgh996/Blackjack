import random

class WordleGame:
    def __init__(self, solution: str, max_attempts: int = 6):
        """
        Parámetros:
        solution (str): La palabra oculta que se debe adivinar.
        max_attempts (int):
        Salida:
        Inicializa el juego con la solución y contador de intentos.
        """

        self.solution = solution.upper()
        self.max_attempts = 6

        self.attempts = []


    # Inicialización de atributos
    def guess(self, word: str) -> dict:
        """
        Realiza un intento de adivinar la palabra.
        Parámetros:
        word (str): Palabra ingresada por el usuario.
        Salida:
        dict: Un diccionario con la evaluación de cada letra
        (por ejemplo: {'letra': 'correcta' / 'mal posicionada' / 'incorrecta'}).
        """
        word = word.upper()
        self.attempts.append(word)
        lista_letras_intento = list(word)
        lista_letras_solucion = list(self.solution)
        print(lista_letras_intento)

        intento = []
        resultado = {}

        for indice in range(5):
            letra = lista_letras_intento[indice]
            letra_solucion = lista_letras_solucion[indice]

            if letra_solucion == letra:
                intento.append('🟢')
                resultado[indice] = {
                    'letra': 'correcta'
                }
            elif letra in lista_letras_solucion:
                intento.append('🟡')
                resultado[indice] = {
                    'letra': 'mal posicionada'
                }
            else:
                intento.append('🔴')
                resultado[indice] = {
                    'letra': 'incorrecta'
                }

        print(intento)
        self.is_finished()
        return resultado

    # Evaluar el intento y retornar el resultado
    def is_finished(self) -> bool:
        """
        Determina si el juego ha terminado (se adivinó la palabra o se acabaron los intentos).
        Salida:
        bool: True si el juego ha terminado, False en caso contrario.
        """
        print(f'Van {len(self.attempts)} intentos')

        if self.solution in self.attempts or self.max_attempts <= len(self.attempts):
            return True

        return False

# Comprobar condición de fin de juego

palabras = ['rumba','tango','perno','perro','marco','pitos','cucas']
palabra_del_dia = random.choice(palabras)
game = WordleGame(palabra_del_dia,6)
while not game.is_finished():
    palabra = input("Ingresa una palabra (5 letras): ")
    if len(palabra) != 5:
        print('Esta palabra no tiene 5 letras')
        continue
    game.guess(palabra)



