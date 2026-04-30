"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one!
    """
    while front_is_clear():
        build_columns()
        safe_move()
        three_steps()
        
def build_columns():
    turn_left()
    build_beepers()
    turn_right()
    move()
    turn_right()
    build_beepers()
    turn_left()
    
def build_beepers():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()

def three_steps():
    if front_is_clear():
        for i in range(3):
            move()

def safe_move():
    if front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
