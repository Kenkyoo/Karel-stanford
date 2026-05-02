from karel.stanfordkarel import *

def main():
    fill_chess_row()
    while left_is_clear():
        reposition_for_next_row()
        fill_chess_row()

def fill_chess_row():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()

def reposition_for_next_row():.
    if facing_east():
        turn_left()
        move()
        turn_left()
    else:
        turn_right()
        move()
        turn_right()

def turn_right():
    for i in range(3):
        turn_left()
if __name__ == '__main__':
    main()
