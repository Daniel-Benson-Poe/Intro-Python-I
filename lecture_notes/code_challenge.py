# UPER
# U: Understanding - Read the problem and understand! Break problem down into easily digestible parts. Draw out examples. etc.
# P: Plan - Plan out your approach. Pseudocode, comments, etc.
# E: 
# R:

def jumping_on_clouds(c):
    # Input: array of 0s and 1s indexed cumulatively
    # 0s safe (cumulus clouds), 1s avoid (thunderhead clouds)
    # Can jump to cumulus clouds (indices) equal to current number plus 1 or 2 - can move one or two spaces forward
    # Find fewest number of jumps required to reach the last cloud
    # Example: x = [0,1,0,0,0,1,0]: Avoid indices 1 and 5. Path can be 0>2>4>6 or 0>2>3>4>6. First path has fewest jumps so would be answer
    # It is always possible to win the game

    # At any cloud we have a choice:
    # jump one cloud away (1 index away) or jump 2 clouds away (2 indices away)
    # Check if the cloud 1 step ahead is valid
    # check if the cloud 2 steps ahead is valid
    # Sometimes we only have one choice
    
    # Trying to find minimum number of jumps
    # This implies it is always better to jump forward two clouds (indices) if we can

    # Always try to jump two clouds away unless it is a thunderhead cloud
    # If cloud two steps away is a thunderhead then jump 1 cloud away

    # Once we reach the last cloud in the list we have won (last cloud should always be 0?)

    # need to keep track of where we are in the path of clouds at any point in time
    # update this variable as we progress through the path of clouds
    current = 0

    # need counter to track number of jumps made
    # increment this every time we make a jump
    jumps = 0

    # keep iterating until we've won the game
    # stop when 'current' == the index of the last cloud

    while current < len(c)-1:
        # check the cloud 2 spots away to see if we can jump there
        if current + 2 < len(c) and c[current + 2] == 0:
            # jump two clouds away
            current += 2
        else:
            # jump one cloud away
            current += 1
        jumps += 1

    return jumps

if __name__ == "__main__":
    input_ex = [0, 0, 1, 0, 0, 1, 0]
    print(jumping_on_clouds(input_ex)) # Should output 4

    input_ex2 = [0,0,0,0,1,0]
    print(jumping_on_clouds(input_ex2)) # should output 3