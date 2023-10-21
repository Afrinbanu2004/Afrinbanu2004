# define the base class Player 
class Player:
     def play (self):
         print("the Player is playing cricket.")
# define the derived class Batsman
class batsman(Player):
     def play(self):
         print("the batsman is batting.")
# define the  derivated class Bowler
class bowler(Player):
     def play(self):
         print("the bowler is bowling.")
# create object of  batsman and bowler classes 
batsman= batsman()
bowler= bowler()

#call the play() method for each object 
batsman . play()
bowler  . play()
