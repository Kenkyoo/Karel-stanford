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
    put_beeper()
    first_row()
    second_row()
    third_row()
    if facing_west():
        big_world()
        go_home()
    else:
        small_world()
        go_home()


def buil_row():
    while front_is_clear():
        if beepers_present():
            move()
        else:
            move()
            put_beeper()

def turn_up():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def check_beeper():
    if beepers_present():
        turn_left()
        if front_is_blocked():
            turn_left()
        else:
            move()
    else:
        turn_left()
        move()
        put_beeper()

def first_row():
    buil_row()
    check_beeper()
    turn_left()

def second_row():
    buil_row()
    turn_up()
    check_beeper()

def third_row():
    turn_right()
    buil_row()
    check_beeper()
    turn_left()

def big_world():
    buil_row()
    turn_up()
    check_beeper()
    turn_right()
    buil_row()
    check_beeper()
    turn_left()
    buil_row()

def small_world():
    turn_right()
    while front_is_clear():
        move()

def go_home():
    turn_left()
    while front_is_clear():
        move()
    turn_left()
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
