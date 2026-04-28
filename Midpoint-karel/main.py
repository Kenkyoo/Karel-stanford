    from karel.stanfordkarel import *
    
    """
    File: main.py
    --------------------
    When you finish writing this file, Karel should be able to find
    the midpoint
    """
    
    def main():
        """
        You should write your code to make Karel do its task in
        this function. Make sure to delete the 'pass' line before
        starting to write your own code. You should also delete this
        comment and replace it with a better, more descriptive one.
        """
        put_beep_corners()
        turn_around()
        move()
        while no_beepers_present():
            move_beepers()
    
        if facing_east():
            if_odd()
        else:
            if_even()
        
    def if_even():
        turn_around()
        move()
        pick_beeper()
        turn_around()
        move()
        turn_around()
    
    def if_odd():
        pick_beeper()
        turn_around()
        move()
        turn_around()
    
    def move_beepers():
        while no_beepers_present():
            move()
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        move()
    
    def put_beep_corners():
        put_beeper()
        while front_is_clear():
            move()
        put_beeper()
    
    def turn_around():
        turn_left()
        turn_left()
    
    if __name__ == '__main__':
        main()
