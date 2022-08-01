#This code is meant to follow our encryption lesson and teach about the automation of encryption.
#This method of encryption is very low level, and for our purposes only allows letters to be encrypted.
#This program works by accessing the numeric value of each letter in the alphablet 1-26.
#It then shifts the letter by a set amount and outputs the shifted letter to the terminal.
#It encrypts each letter one at a time until each letter has been shifted and output.



alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Strings can be accessed same way arrays are
shiftKey = 5 #How many letters you want your word to shift by
password = input("Enter your password\n") #let user enter their password
letterIndex = 0 #used to index through the word

while letterIndex < len(password): #This is just saying, keep encrypting the word as long as there are letters
    place = alphabet.lower().find(password[letterIndex]) #find what number the letter is in the alphabet
    encrypted = place + shiftKey #add the shiftkey to the letters # in the alphabet
    #E.g J is the 10th letter, with shiftKey added, it would be the 15th letter.


    #If the new letter is past Z, we want to start back at the beginning and keep going
    if encrypted > 26:
        encrypted = encrypted - 26
    #finally just print out the new encrypted key
    print(alphabet[encrypted], end="")

    #That was all for the first letter, add to the letterIndex to do this process for each letter in password
    letterIndex += 1 
    