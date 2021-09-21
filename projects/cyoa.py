"""The Haunted House Adventure."""

__author__ = "730319741"

points: int = 0
player: str = ""
ghost: str = "\U0001F47B"
i: int = -1
 

def greet() -> None:
    """The program's greeting."""
    global ghost 
    print(f"{ghost}Welcome to the Haunted House Adventure... ")
    print("If you choose to play, the rules are simple... ")
    print("1. Make decisions based on the prompts given. Choose your fate wisely. ")
    print("2. There are no wrong decisions, but there will be times where the options given will result in Game Over. ")
    print("3. Every time you advance on to the next set of options, one point will be awarded. You begin with 0 points each time you play. ")
    print("4. Never divulge the secret to escaping the House... The consequences that follow will haunt you forever. ")
    print(f"Continue at your own risk. {ghost} ")
    global player 
    player = str(input("Enter your name: "))


def main() -> None:
    """The program's entry point."""
    global ghost
    greet()
    con: str = input(f"Would you like to start enter the Haunted House? {ghost} ")
    global points
    while con == "yes": 
        points = 0
        print(f"You are now entering the House. {ghost} ")
        choice_1()
        con = input(f"Do you want to play again, yes or no? {ghost} ")
    

def choice_1() -> None: 
    """The first choice given after entering."""
    global points
    global player
    global ghost
    print("So " + player + ", you have decided to try escaping from the Haunted House. ")
    print("You begin in the main hall, where you are met with three doors; the left door is #1, the middle door is #2 and the right door is #3. ")
    c1: int = int(input(f"What door do you choose? {ghost} "))
    if c1 == 1:
        cavern_room()
    else:
        if c1 == 2:
            hallway_1()
        else:
            points = points + 4
            game_won()
               

def cavern_room() -> None:
    """What happens if door 1 is chosen."""
    global points
    print("You stepped through the door and there is a pit of lava in front of you. To your right there are two dice and you roll them.")
    from random import randint
    roll: int = randint(2, 12)
    if roll >= 6:
        print(f"The number you rolled was {roll}, which means you chose to walk around the pit of lava to the door across from you. ")
        points = points + 1
        final_door()
    else:
        print(f"Ther number you rolled was {roll}, which was means you slipped and fell into the lava. ")
        game_over()
    

def hallway_1() -> None:
    """What happens if door 2 is chosen.""" 
    global points 
    points = points + 1
    choice_2: str = input("You now come to a hallway with two doors, one blue and one green. Which do you choose? ")
    if choice_2 == "blue":
        points = points + 1
        final_door()
    else:
        if choice_2 == "green":
            points = points + 3
            game_won()

                
def game_over() -> None: 
    """What happens if an incorrect choice is made."""
    global points
    print("Points: " + str(points))
    print(f"Game over... Try again if you dare. {ghost}")


def final_door() -> None: 
    """The last choice that is made to either game over or game win."""
    global ghost
    global points
    points = points + 1
    print("At this next set of doors, you can hear faint screaming coming from one of them but it is unclear which one.")
    choice_2: str = input("Which door do you chose; left or right? ")
    if choice_2 == "left":
        points = points + 2
        a: int = int(input("Pick a random number: "))
        b: int = int(input("Choose a second random number: "))
        z: int = max(a, b)
        points = points + z
        print(f"You have been given {str(z)} extra points for making it this far. ")
        game_won()
    else:
        if choice_2 == "right":
            points = points
            print("You fell into a pit of lava. ")
            game_over()


def max(a: int, b: int) -> int:
    """Returns largest number player picked."""
    if a >= b:
        return a
    else:
        return b
        

def game_won() -> None:
    """What happens if the Haunted House is escaped."""
    global points
    global player
    global ghost
    print(f"Congratulations, {player} you made it out of the Haunted House alive! {ghost} ")
    print(f"Total points: {str(points)}")
    

if __name__ == "__main__":
    main()