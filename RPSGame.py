from os import system
import random
class RPSGame(object):
    """ The rock, paper, and scissors game class"""

    AICHOICES = ["Rock", "Paper", "Scissors"]

    CHOICES = ["Rock", "r", "Paper", "p", "Scissors", "s"]

    def getWinner(self, rps, AIrps):
        print("Your choice: ", rps)
        print("AI choice: ", AIrps)
        if((rps == "Rock" or rps == "r") and (AIrps == "Paper")):
            #user loses
            print("You have lost", AIrps, "covers Rock")
        elif((rps == "Rock" or rps == "r") and (AIrps == "Rock")):
            #user ties
            print("It is a tie")
        elif((rps == "Rock" or rps == "r") and (AIrps == "Scissors")):
            #user wins
            print("You win Rock crushes Scissors")
        
        elif((rps == "Paper" or rps == "p") and (AIrps == "Scissors")):
            #user loses
            print("You have lost", AIrps, "gets cut by Scissors")
        elif((rps == "Paper" or rps == "p") and (AIrps == "Paper")):
            #user ties
            print("It is a tie")
        elif((rps == "Paper" or rps == "p") and (AIrps == "Rock")):
            #user wins
            print("You win Paper covers Rock")

        elif((rps == "Scissors" or rps == "s") and (AIrps == "Rock")):
            #user loses
            print("You have lost", AIrps, "crushes Scissors")
        elif((rps == "Scissors" or rps == "s") and (AIrps == "Scissors")):
            #user ties
            print("It is a tie")
        else:
            #user wins
            print("You win Scissors cut Paper")

        return

    def startNewGame(self):
       choice = ""
       AIChoice = random.choice(RPSGame.AICHOICES)
       system("cls")
       while(choice is not 0):
           choice = input("""The game has begun. 
    Rock    | r - Rock
    Paper   | p - Paper
    Scissor | s - Scissors

After you have made your choice, you will know if you have won.
You may also enter 0 to quit

Please make your choice: """)
           if(choice == "0"):
               quit()
           elif(choice.capitalize() not in RPSGame.CHOICES):
               print("please enter a valid response")
           else:
               self.getWinner(choice, AIChoice)
               keepPlaying = True
               while(keepPlaying):
                   keepPlaying = input("Would you like to keep playing? (y or n) ")
                   if(keepPlaying == "yes" or keepPlaying == "y"):
                       self.startNewGame()
                   elif(keepPlaying == "no" or keepPlaying == "n"):
                       quit()
                   else:
                       print("Please enter a valid response")
           
           


