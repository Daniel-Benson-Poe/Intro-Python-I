# Checked code in all previous exercises and this one
# to ensure they were up to Pep8 standards.

"""
The Sieve of Eratosthenes allows us to find all prime numbers in a list
of consecutive numbers of length n. We start with the smallest number
and iterate through all of its multiples, excluding itself, crossing
each of them off the list. We then move to the next closest number
not crossed off and repeat the above process until we have gone
through all the numbers. At this time any remaining numbers not
crossed off are prime numbers.
"""


def sieve_of_erat(n):  # Takes in a number n as an end point
    # Create a list of True values having index i[0...n]
    # All values in the list will be True until proven not to be prime
    num_list = [True for num in range(0, n+1)]
    # Set smallest_num to first number we want to test (2...n)
    smallest_num = 2
    while smallest_num * smallest_num <= n:  # Check we are still in bounds
        # Check that num in the list has not been crossed off
        if num_list[smallest_num] == True:
            # Iterate through all multiples of smallest_num
            for i in range(smallest_num * 2, n + 1, smallest_num):
                # Change all multiples of smallest_num to False
                num_list[i] = False
        # Increment smallest_num by 1
        smallest_num += 1
    # Because we are ignoring 0 and 1,
    # manually set those positions in the list to False
    num_list[0] = False
    num_list[1] = False
    # Print out our list of prime numbers
    for num in range(0, n+1):
        if num_list[num]:
            print(num)

if __name__ == "__main__":
    sieve_of_erat(120)
