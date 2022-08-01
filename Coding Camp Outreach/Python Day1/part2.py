#we have learned a fair bit of basics, but in order for us to make our code a lot more concise,
#we need to learn a few more difficult but fairly straightforward concepts
#First is lists.
#You can think about lists as a variable that holds more than one item. 
#Create a list by putting square brackets around each value seperated by commas.


myList = ["yah", "yuh", 30]
print(myList)
#You can do some cool things with lists that make them powerful. 
#We can add to our list using list.append
myList.append("Heyo")
print(myList)
#you can also access certain elements in the list
#It is important to note that lists start with 0 and count up from there.
#so in our case, "yah" would be the 0th element, "yuh" the 1st, 30 the 2nd, and "Heyo" the third
#Our lists counts from 0-3, despite being four values long
#We can access a certain value from our list like so. Don't worry we will practice this is a second.
print(myList[0])
print(myList[3])
#To practice this, lets make a new list with all the letters of the alphabet
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#with this, try spelling out your name by accessing each element and writing it out with print functions
#Remember, the list goes from 0-25 to account for 26 letters
print(letters[9])
print(letters[14])
print(letters[4])
#Sorry but I actually just wasted a bit of your time. I should have told you that strings work the same way
#You can access characters (usually letters) in a string by using their number in order as you do a list.
#if we make a new String just typing A-Z, we can use our same print statements and get the same output.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(letters[9])
print(letters[14])
print(letters[4])

#one more fun project we can make is a magic 8 ball. 
#for this we need to intorduct a built in python module that will give us a random number in a set range.
import random
#imports come with built in functions that add personality to your projects and help developers save time
#We use the name of the import to use its functions.
#for our 8ball, we are going to get a random number between 1 and 7, because our list will be 8 values long
randomNum = random.randint(0,7) 
print(randomNum)
#If we run this a few times, we will see that we get a random number in our set range.
#now to put this number to use, we will make a list of possible responses for our 8ball
responses = ["Yes", "It is certain", "Absolutely", "Ask again later", "It is possible", "It is unlikely", "Immediately No", "No bozo"]
#Remember that the list numbers range from 0 to 7, so our random number will access one of the answers
#We also need to ask the user to enter their yes or no question. 
#We will use our old friend the input function to help us out
question = input("Enter a Yes or No question")
#now we can simply print out our answer given to us by our random number
print(responses[randomNum])


#We need to learn some ways of comparing things 
#There are things called if statements that are incredibly useful
#Lets say we have two numbers and we wanted to tell a user if the first is greater than or less than the second
#For this, lets make 2 int variables and we can compare them
num1 = 40
num2 = 30 
#now we have comparitors just like we do in math, <, >, =, <=, and >=
#We can use if statments to check some of these things
if num1 > num2: #If this
    print(f"{num1} is greater than {num2}") #Then this
#This is a good time to bring indentation to your attention. 
#run our program now and it should work, remove the space before our print line and our code will break
#While many languages use { } brackets to seperate code blocks, python uses indentation
#You want everything indented to happen only if the comparison is true.
#so our code works right now, but if our num1 is less than our num2 nothing will happen
#We need to check if its smaller using another if statement
if num1 < num2: #If this
    print(f"{num1} is less than {num2}") #Then this
#We also need to check if the two numbers are equal
if num1 == num2: #If this
    print(f"{num1} is equal to {num2}") #Then this

#While this works, there is a better way to go about this, we can use elif (else if) and else staements
#Before that, though lets let the user decide the numbers
num1 = input("Enter a number")
num2 = input("Enter a number")
#now we check if these are equal to, less than, or greater than one antoehr
if num1 == num2: #We use == to compare to things because a single = is already used for creating variables
    print(f"{num1} is equal to {num2}")
elif num1 >= num2: #Else if. just another if statement in the same thing
    print(f"{num1} is greater than {num2}")
else: #Else is a catchall block that outputs if every other specified case  
    print(f"{num1} is less than {num2}")

#There is also an extra one (!=) that means does not equal
if num1 != num2:
    print(f"{num1} is not equal to {num2}")
else:
    print(f"{num1} is equal to {num2}")

#you can also use the keywords or/and to compare two things in a single if statement. 
if int(num1) > 20 and int(num1) < 50: #Cast to int because input gives us strings
    print(f"{num1} is between 20 and 50")
if num1 == 20 or num1 == 50:
    print(f"{num1} is either 20 or 50")


#Now we are going to go over while and for loops
#While loops say, do this while a condition is true. 
#you can have something run forever, or a certain amount of times. 
#You can dirctly code while True to have something run forever, or do something like

increasingNumber = 0
while increasingNumber <= 20: #While our number is less than 20
    print(increasingNumber)
    increasingNumber += 1 #Increase the number by 1 each time so it doesnt run forever.


#Next is for loops.
#For loops require a stopping point in your code, so it's not possible (kinda) to be able to run forever like a while loop.

for number in range(10): #Bascially saying for a variable in the range 10, print the variable.
    #Also can be seen as bascially do whatever is indented 10 times over.
    print(number)

#This is the end of part 2. 
#There is more yet but this is the extent that we learned in class






