def main():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    print ('This program will add or multiply two numbers together, and ask you for the answer. \nThe program will quit after five correct answers')
    choice = int(input('Choose 1 for addition or 2 for multiplication: '))
    while counter1 + counter2 < 5:
        num1 = int(input('Enter your first number: '))
        num2 = int(input('Enter your second number: '))
        add = num1 + num2
        mult = num1 * num2
        if choice == 1:
             answer1 = int(input('What is the answer? '))
             #debug by dumping your variables to the screen as you progress through the script
             print ('Dump after user enters 1 - counter1 ' counter1:, ' counter2: ',counter2, 'counter3: ',counter3, 'counter 4: ',counter4,'num1: ',num1,'num2: ',num2'\n')
             if answer1 == add:
                 counter1 = counter1 + 1
                 print ('Correct Answer') 
            else:
                counter3 = counter3 + 1
                print ('Incorrect Answer')        
            #maybe need to add "choice = int(input('Choose 1 for addition or 2 for multiplication: '))" here as well?
        else: #may have to make this an "if" statement to force it to go down to "choice" input statement
            answer2 = int (input('What is the answer? '))
            #debug by dumping your variables to the screen as you progress through the script
            print ('Dump after user enters 1: counter1: ' counter1, ' counter2: ',counter2, 'counter3: ',counter3, 'counter 4: ',counter4,'num1: ',num1,'num2: ',num2'\n')
            if answer2 == mult:
                counter2 = counter2 + 1
                print ('Correct Answer')
            else:
                counter4 = counter4 + 1
                print ('Incorrect Answer') 
    #why is choice here again? choice is defined outside the while loop at the top of the script...
        choice = int(input('Choose 1 for addition, 2 for multiplication '))
    print ('The number of problems answered are listed below:\n')
    print ('The number of correct addition problems answered: ',counter1,'\n')
    print ('The number of incorrect additions problems attempted: ',counter3,'\n')
    print ('The number of correct multiplication problems answered: ', counter2,'\n')
    print ('The number of incorrect multiplication problems answered: ',counter4,'\n')

main()