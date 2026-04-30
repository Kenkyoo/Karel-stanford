"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

def main():
    degrees_fahrenheit = int(input("Enter temperature in Fahrenheit: "))
    degrees_celcius = (degrees_fahrenheit - 32) * 5.0/9.0
# There is no need to edit code beyond this point
    print(f"Temperature: {float(degrees_fahrenheit)}F = {degrees_celcius}C")
if __name__ == '__main__':
    main()
