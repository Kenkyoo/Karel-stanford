# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    value_as_str = input("Enter an age in calendar years: ")
    value_as_number = float(value_as_str)
    dog_age = value_as_number * 7.18
    print(f"That's {dog_age} in dog years!")
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
