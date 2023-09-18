#2.2 implement a class called player that represents a cricket player. The player class should have a methos called play() which prints “the player is playing cricket. Derive two classes,batsman and bowelwr, from the player class. Override the play() method in each detived calss to print” the batsman is batting”and “the bowling is bowling”, respectively. Write a program to create objects of both the batsman and bowler classes and call the play() method for each object.

#define the player class

Class player:
def play(self):
print("the player is playing cricket.")
#define the batsman class, derived from player
Class batsman(player):
def play(self):
print("the batsman is batting.")
#define the bowler class, detived from player
Class bowler(player):
Def play(self):
print("the batsman is bowling.")
#define the bowler class,derived form player
Class bowler(player):
def play(self):
print("the bowler is bowling.")
#create objects of batsman and bowler 
classes 
Batsman=batsman()
Boweler=bowler()
#call the play()method for each object
Batsman.play()
Bowler.play()
