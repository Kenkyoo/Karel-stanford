from karel.stanfordkarel import *

def main():
    while front_is_clear():
        stairs()
    put_beeper()

def stairs():
    step_up()

def turn_right():
    for i in range(3):
        turn_left()

def step_up():
    put_beeper()
    move()
    turn_left()
    move()
    turn_right()

# don't change this code
if __name__ == '__main__':
    main()
