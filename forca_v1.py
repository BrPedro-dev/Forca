# Hangman Game (Jogo da Forca)

# Import
import random, argparse, sys


# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = list(word)
        self.word1 = word
        self.missed_letter = []
        self.guessed_letter = []
        self.contador = 0

    # Método para adivinhar a letra
    def guess(self, letter):
        self.letter = letter
        if letter in self.word and letter not in self.guessed_letter:
            return self.guessed_letter.append(letter)
        else:
            self.contador += 1
            return self.missed_letter.append(letter)

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if self.hangman_won() or self.contador > 6:
            return True
        return False

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if "_" not in self.hide_word():
            return True
        return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        hide_letter = " "
        for letter in self.word:
            if letter not in self.guessed_letter:
                hide_letter += "_"
            else:
                hide_letter += letter
        return hide_letter

    def lista_missed(self):
        missed_list_organized = ""
        for elementos in self.missed_letter:
            missed_list_organized += elementos + " "
        return missed_list_organized

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        if self.contador <= 6:
            print(board[self.contador])
        print(f"\nA palavra secreta é : {self.hide_word()}")
        if self.hangman_over() is False:
            print(
                f"\nAs letras erradas que já foram utilizadas: "
                f"{self.lista_missed()}"
                )


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    parser = argparse.ArgumentParser(description = 'Jogo da Forca')
    parser.add_argument('--path', default='palavras.txt', help='')
    args = parser.parse_args()
    try:    
        with open(args.path, "rt") as f:
            bank = f.readlines()
        return bank[random.randint(0, len(bank))].strip()
    except FileNotFoundError: 
       print(f'Arquivo {args.path} não encontrado')
       sys.exit(1)

# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma
    # letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        user_input = str(input("Qual é a letra? ")).lower()
        game.guess(user_input)

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word1)


# Executa o programa
if __name__ == "__main__":
    main()
