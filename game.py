#importing the time module
import time
#import random function
import random

#welcoming the user

name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman!")
print ("(1)Yes, for I am pretty 1 bright .\n(2)No, get me outta here!")
user_choice_1 = input("->")
		
if user_choice_1 == '1':
        print("Get ready to die then and there is no escape")
	
elif user_choice_1 == '2':
	print("Bye bye now...")
	exit()
else:
	print("I'm sorry, I'm hard of hearing, could you repeat that?")
	self.__init__()

def playagain():
        
        print("")

        #wait for 1 second
        time.sleep(1)

        print("Start guessing...")
        time.sleep(0.5)

        #here we set the word to be guessed
        words = ['secret','books','python','character','computer','program','ephraim','campus','game','school','table','esther',]
        word = random.choice(words)

        #creates an variable with an empty value
        guesses = ''

        #determine the number of turns
        turns = 7

        # Create a while loop

        #check if the turns are more than zero
        while turns > 0:         

                # make a counter that starts with zero
            failed = 0             

            # for every character in secret_word    
            for char in word:      

            # see if the character is in the players guess
                if char in guesses:    
    
                # print then out the character
                    print (char)    

                else:
    
                # if not found, print a dash
                    print("_")     
       
                # and increase the failed counter with one
                    failed = failed + 1    

            # if failed is equal to zero

            # print You Won
            if failed == 0:        
                print("You won")
                print("Congratulations, do you want to play again")
                y = int(input("if yes enter 1, if no enter 0"))
                if y==0:
                        print("exit")
                        exit
                else:
                        playagain()
                
                


            # exit the script
                break              

            print

            # ask the user go guess a character
            guess = input("guess a character:") 

            # set the players guess to guesses
            guesses += guess                    

            # if the guess is not found in the secret word
            if guess not in word:  
 
             # turns counter decreases with 1 (now 9)
                turns -= 1        
 
            # print wrong
                print("Wrong")
    
 
            # how many turns are left
                print("You have", + turns, 'more guesses')
 
            # if the turns are equal to zero
                if turns == 0:           
    
                # print("You Loose"
                    print("You Loose")
                    print("Do you want to hang again?????")
                    x = int(input("If yes enter 1, if no enter 0"))
                    if x == 0:
                        print("Sorry, better luck next time, Bye bye.....")
                        exit()
                    else:
                        playagain()

playagain()
                
                
                
                
                         
