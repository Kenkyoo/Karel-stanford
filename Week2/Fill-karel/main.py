from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while no_beepers_present():
        fill_karel()
    while front_is_clear():
        move()

def build_row():
    while front_is_clear():
        put_beeper()
        move()

def turn_back():
    turn_left()
    turn_left()
    put_beeper()

def moving():
    while front_is_clear():
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def fill_karel():
    build_row()
    turn_back()
    moving()
    turn_right()
    if front_is_clear():
        move()
    turn_right()    

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
