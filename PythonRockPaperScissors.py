# a Rock, Paper, and Scissors game made in Python
import RPSGame
print("""
            Welcome to the Python Rock, Paper, and Scissors Game
            
            Just pick Rock, Paper, or Scissors and see if you win
""")

play = True
game = RPSGame.RPSGame()
while(play):
    game.startNewGame()
    keepPlaying = input("Would you like to play again? (y or n)")
    play = True if (keepPlaying == "yes" or keepPlaying == "y") else False