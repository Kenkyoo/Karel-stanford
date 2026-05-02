from karel.stanfordkarel import *

def main():
    move()
    if beepers_present():
        pick_beeper()  
        if beepers_present():
            pick_beeper()
            if beepers_present():
                pick_beeper()
    move()
    move()
    if beepers_present():
        pick_beeper()
        pick_beeper()
        pick_beeper()
        pick_beeper()

    move()
    move()
    if beepers_present():
        pick_beeper()
    move()

if __name__ == "__main__":
    main()
