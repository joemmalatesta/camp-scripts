import random
while True:
    question = input("Enter a Yes or No question\n") #have user enter a question and store it as a variable.
    randomNum = random.randint(0,7) #Pick a random number, 0 to 7
    answers = ["Yes", "sure", "of course", "Maybe", "perhaps", "negative", "no", "probably not"]
    print(answers[randomNum]) #Print out an asnwer from the array of options using our random number.


#much simpler than java, right :)