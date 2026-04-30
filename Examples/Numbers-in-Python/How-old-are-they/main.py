"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def main():
    names = [
        {"name": "Anton", "age": 21},
        {"name": "Beth", "age": 21 + 6},
        {"name": "Chen", "age": 27 + 20},
        {"name": "Drew", "age": 47 + 21},
        {"name": "Ethan", "age": 47},
    ]

    for person in names:
        print(f"{person['name']} is {person['age']}")
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
