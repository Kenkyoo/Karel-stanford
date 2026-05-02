from karel.stanfordkarel import *

def main():
    move()
    if beepers_present():
        while front_is_clear():
            pick_beeper()
    move()
    move()
    if beepers_present():
        pick_beeper()
    move()

if __name__ == "__main__":
    main()
