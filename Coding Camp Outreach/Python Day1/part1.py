#This will be an introduction to python split into several parts
#comments will explain code that builds upon itself before each section and in the line if necessary.


#This is python. Python was created by Guido van Rossum and was named after Monty Python's Flying Circus
#Fun fact, the word 'Spam' was also popularized in computer jargon from a monty python script. 


#Python is used in Google, Netflix, Spotify, automating Teslas, and much much more
#This is an introduction to python going over what is useful and practical.


#The first section will be going over your first program, variables, and simple equations

#The first program you will write is a simple print fucntion. 
#Programs are simply instructions written by you that your computer and understand and run 

#Print simply takes whatever you put in the (" ") and outputs it in your terminal.


print("hello world") #Type this out and then press F5 to run the program

#As you can see, the word print is highlighted/green. This is because it is a word recognized by python
#Python is case sensitive with these words, so if you tried typing Print("hello world") it would not work


#VARIABLES
#imagine variables as a named box with something in it, be it words, numbers, or a True or false value
sentence = "Hi, this is the computer speaking" #This is a String (str)
print(sentence)
number = 416 #Integer, cannot be decimal
print(number)
decimalNumber = 3.14 #Float, can be decimal
print(decimalNumber)
lightSwitch = True #Boolean (bool in python) only be True or False. 
print(lightSwitch)

#If we type print(type(variable)) it will show us the type of variable we are using.
print(type(sentence))
print(type(decimalNumber))


#Now you may think this is dumb and why can't we just type what we want instead of using variables.
#The power of variables comes from their ability to be reused throught the code so you only have to write it once
#As well as their ability to be updated or changed later in the code
#You always want your variables to be descriptive so you dont confuse yourself later.


#Say for exmaple there was a number that counted every person in Michigan
rochesterPopulation = 74300
print(rochesterPopulation)
#now imagine we had to manually update the number everyime someone was born in Rochester.
#instead we can use math operations to increase the number
rochesterPopulation = rochesterPopulation + 1
print(rochesterPopulation)
#This can also be written as
rochesterPopulation += 1
print(rochesterPopulation)


#Your computer is also capable of computing math equations
#You can use operators like plus (+), minus (-), multiply(*), and divide(/)
num1 = 40
num2 = 5
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

#But what if we had a string with the value "40" and we tried to add it to a number
num1 = "40"
#print(num1 + num2)
#if we try this now, it will give us an error showing saying you can't add words to numbers
#we need to do something called type casting.

#if we check the type of the variable num1, it will tell us it is a string
print(type(num1))
#in order to change this and be able to use it as an integer we need to cast our string to an int by doing
num1 = int(num1)
print(type(num1))
#This is explicitly telling our program that we want our variable to be used as an integer
#now if we check the type it will tell us this is an int, and we will be able to use it in math equations

print(num1 + num2) 
 

#One more thing we need to introduce before starting our first small projects is the input() method.
#the input method allows the user to type into the output and have their input be used in the code
name = input("What is your name? ")
print(name)
#The problem is that the input fucntion treats everything as words.
#Even if you enter a number, it will be treated as a string, so we have the same issue as above.


#With this, we can make a simple addition calcualator
firstNum = input("enter your first number ")
secondNum = input("Enter your second number ")
#print(firstNum + secondNum)
#but as epxected, when we try to add these, its saying it can't add two things that are strings.
#because of this, we need to use our type casting to change our strings into ints.
firstNum = int(firstNum)
secondNum = int(secondNum)
#now we can add these together and save the total in a third variable called sum
sum = firstNum + secondNum
print(sum)
#now try out your code and see that it runs


#With variables, we can have them output alongside text that you type into a print fucntion.
#Because we are using these numbers in a string, though, we need to cast them back into integers
#We can do that inside of the print function just as we have been before
print(str(firstNum) + " Plus " + str(secondNum) + " Eqauls " + str(sum))


# This can also be written with something called an F string
#by including an f before the quotation marks inside the parentheses
#you can include variables in the output without having to use the + by putting them in squiggly brackets
print(f"{firstNum} Plus {secondNum} Equals {sum}")
#as yo can see, even though we didn't cast these numbers to strings, it still outputs the numbers all the same
#This makes using f strings the obvious choice for me, but there still is an option


#To continue practice with this, we can make a mad libs game
#Write a story with a few blanks and let the user choose words to fill in the story
#Open madlibs.py to continue