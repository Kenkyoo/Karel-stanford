from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    move()
    # your code here
    for i in range(10):
        # things to repeat
        pick_beeper()
    move()
    move()
    for i in range(10):
        # things to repeat
        pick_beeper()
    move()
    move()
    for i in range(10):
        # things to repeat
        pick_beeper()
    move()
'''
def picker(n):
    for i in range(n):
        # things to repeat
        pick_beeper()   
'''
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
