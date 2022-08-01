import random #For our use, making an array of 5 letter words works, but there is a module for it
possibleWords = ["shone", "trail", "mouse", "heads", "brain", "irate", "loser", "bozos", "mouth"]
number = random.randint(0,8)
word = possibleWords[number] #Select a random word from our array and have that be the answer
guessCount = 0 #up to 5
hiddenWord = ["*","*","*","*","*"] #Keep hidden until letters are guessed


while guessCount < 5: #5 lives
    guess = input("Enter a 5 letter word\n")
    guess = guess.replace(" ", "") #Incase there is spaces added to the guess
    if guess == word: #if they guessed the word, finish the code
        print("You guessed it, good job")
        break
    if len(guess) != 5: #If they entered an invalid word, continue without removing a guess.
        print("Enter a FIVE LETTER word") #Remind it needs to be 5 letters
        continue
    wordIterator = 0 #Used to iterate through the answer letter by letter.
    while wordIterator != 5: #whatever is in here happens to each letter, one by one
        for letter in guess: 
            if letter == word[wordIterator]: #Check if any letter in your guess is in the asnwer
                hiddenWord[wordIterator] = letter #replace the correct letter in the hidden output.
        wordIterator += 1 #Continue to next letter in the answer
    print(hiddenWord) #After each guess, print the hidden word showing their revealed letters
    guessCount += 1 #decrease guess count and print how many guesses left
    print(f"\nYou have {5-guessCount} guesses left")
    #End while loop

if guessCount == 5: #If you ran out of guesses, end the program and tell the user the word
    print(f"You didn't get it!\n the word was {word}")

