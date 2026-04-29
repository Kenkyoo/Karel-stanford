"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Places beepers in a zig zag pattern.
    """
    while front_is_clear():
        zig()
        zag()
        
def zig():
    put_beeper()
    safe_move()
    up()

def zag():
    put_beeper()
    safe_move()
    down()

def safe_move():
    if front_is_clear():
        move()

def up():
    turn_left()
    move()
    turn_right()

def down():
    turn_right()
    move()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
