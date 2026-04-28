import random

def main():
    # input always gives a value of type string
    value_as_str = input("How many sides does your dice have? ")

    # you can change the string to a float
    value_as_number = int(value_as_str)

    rand_num = random.randint(1, value_as_number)

    print(f"Your roll is {rand_num}") 
if __name__ == '__main__':
    main()
