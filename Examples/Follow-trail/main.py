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
    comment and replace it with a better, more descriptive one.
    """
    while beepers_present():
        follow_straight_trail()
        step_backwards()
        check_beeper()

def check_beeper():
    turn_left()
    move()
    if no_beepers_present():
        trail_right()

def trail_right():
    turn_around()
    for i in range(2):
        move()

def follow_straight_trail():
    while beepers_present():
        pick_beeper()
        move()

def turn_around():
    for i in range(2):
        turn_left()

def step_backwards():
    turn_around()
    move()
    turn_around()

def turn_right():
    for i in range(3):
        turn_left()
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
