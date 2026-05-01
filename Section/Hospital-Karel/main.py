from karel.stanfordkarel import *

# Here is a place to program your Section problem

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        go_to_position()
        build_hospital()
        safe_move()
        
def go_to_position():
    while no_beepers_present():
        move()

def build_hospital():
    turn_left()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_left()

def safe_move():
    if front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    main()
