import time  #import time to slow down the printing. Show what it does without it first, then introduce time module.
indentIncreasing = True #This works as an on and off switch or an increasing or decreasing boolean. 
indent = 0 #The amount of space in front of the stars


while True: #Make it run forever
    print(" " * indent + "**********") #first output the stars with no indent... (" " * indent) creates empty space before the stars 
    time.sleep(.02) #DO THIS STEP LAST. slows down the printing. let them play around with the speed

    #LOGIC
    if indentIncreasing == True: #Auto set to true, so basically when this runs
        indent += 1 #Add one to the indent variable, should have gone over this prior.
        if indent == 15: #Making it so that the above code runs only 15 times
            indentIncreasing = False #Once indent reaches 15, the switch is turned off, and the indent starts going back to 0


    if indentIncreasing == False: #once indent is 15
        indent -= 1 #Decrease the indent back towards 0
        if indent == 0: #Stop the indent at 0 and turn the switch back on. 
            indentIncreasing = True #TURN IT BACK ON!