score = 0

def add_points(points):
    global score
    score += points
    print("Score is now:", score)

def game_round():
    score = 100

    def bonus():
        nonlocal score
        score += 10
        print("Round score:", score)
    
    bonus()
    print("After bonus, round score:", score)

"""
Broken scope error:
def reset():
    score = 0
"""

#FIX:
def reset():
    global score
    score = 0

while True:
    print("\n1. Add points")
    print("2. Play round")
    print("3. Reset score")
    print("4. Show score")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        pts = int(input("Points to add: "))
        add_points(pts)
    
    elif choice == "2":
        game_round()

    elif choice == "3":
        reset()
    
    elif choice == "4":
        print("Global score:", score)
    
    elif choice == "5":
        break

    else:
        print("Invalid choice")