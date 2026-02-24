"""
#BROKEN CODE:

counter = 0

def increase():
    counter = counter + 1
    print(counter)

increase()
"""

#fix:
counter = 0

def increase():
    global counter
    counter = counter + 1
    print(counter)

increase()