import random

HANGMAN_PICS = [ '''
    +---+
         |
         |
         |
         ===''','''
    +---+
    O    |
         |
         |
         ===''','''
    +---+
    O    |
    |    |
         |
         ===''','''
    +---+
    O    |
   /|    |
         |
         ===''','''    
    +---+
    O    |
   /|\   |
         |
         ===''','''        
    +---+
    O    |
   /|\   |
   /     |
         ===''','''    
    +---+
    O    |
   /|\   |
   / \   |
         ===''']
words = 'giggle picnic cozy fluffy chirp splash sleepy swing explore melody dream cloud flower kite puddle teacup train cake candy cookie ice cream pizza soup  cat dog fish horse owl rabbit turtle'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print('\n', HANGMAN_PICS[len(missedLetters)], '\n')
    print("\nMissed Letters: ", end = '')
    print()
    for letter in missedLetters:
        print(letter, end = '')
    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end = '')
    print()

def getGuess(alreadyGuessed):
    while True:
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        if len(guess) != 1:
            print("Only single letter is allowed.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter! Choose again.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a letter! Chosse again.")
        else:
            return guess
        
def playAgain():
    print("Would you like to play again? (Yes/No)")
    return input().lower().startswith('y')

print('|_H_A_N_G_M_A_N_|')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("You guessed it!!")
            print(f"The secret word is {secretWord} ! YOU WIN !" )
            gameIsDone = True
        else:
            missedLetters = missedLetters + guess
            if len(missedLetters) == len(HANGMAN_PICS) -1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print(f"You have run out of guesses!\nAfter {str(len(missedLetters))} missed guesses and {str(len(correctLetters))} correct guesses, the word was {secretWord} ")
                gameIsDone = True
        
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break