'''6. Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.

Dica: Você precisará importar uma biblioteca para resolver esse
exercício'''

from random import choice
from hangman_words import word_list
from hangman_arts import logo, stages

print(logo)
word = choice(word_list)
word_length = len(word)
display = ['_' for _ in range(word_length)]
end_of_the_game = False
lives = 6
guessed_letters = []  

print(' '.join(display))

while not end_of_the_game:

  guess = input('Guess a letter: ').lower()

  if guess in guessed_letters:
    print(f"You've already chosen the letter '{guess}'. Try again.")
    continue

  guessed_letters.append(guess)

  if guess not in word:
    print(f"You guessed '{guess}', that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      end_of_the_game = True
      print(f"GAME OVER. YOU'VE LOST! The word was '{word}'.")
      break

  for position in range(word_length):
    letter = word[position]
    if letter == guess:
      display[position] = letter

  print(' '.join(display))

  if '_' not in display:
    end_of_the_game = True
    print('CONGRATULATIONS! You win!')

  print(stages[lives])