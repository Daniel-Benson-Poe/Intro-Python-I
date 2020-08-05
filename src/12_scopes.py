# Experiment with scopes in Python.
# Good reading:
# https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12


def change_x():
    global x
    x = 99

change_x()

# This prints 12. What do we have to modify
# in change_x() to get it to print 99?
print(x)
# In our function we used the "global" keyword
# to call in the global variable of x (with its value of 12).
# now by changing the value of x
# in the function it changes the value of x globally as well.

# This nested function has a similar problem.


def outer():
    y = 120

    def inner():
        nonlocal y
        y = 999

    inner()

#     # This prints 120. What do we have to
#     # change in inner() to get it to print
#     # 999?
#     # Note: Google "python nested function scope".
# We call nonlocal variable for y which allows
# us to change the value in y from the outer() function
    print(y)


outer()
