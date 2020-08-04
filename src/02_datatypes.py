"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

def int_val():
    print(x + int(y))


# Write a print statement that combines x + y into the string value 57

def string_val():
    print(str(x) + y)

def error_proof():

    try:
        x + y
    except(TypeError):
        print("You received a type error! You can't add a string and an integer together.")

if __name__ == "__main__":
    error_proof()
    int_val()
    string_val()
