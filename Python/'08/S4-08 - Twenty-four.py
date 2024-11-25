# By: Kevin Xia
# Solution: DFS (find every possibilty and evaluate, time limit allows for this)

import sys

input = input = sys.stdin.readline # unnecessary but works
ans = None

def begin_solving(nums): # start function to help the process
    for num in nums: # attempt the twenty four function with every possible starting number
        nums_left = nums[:]
        nums_left.remove(num)
        twentyfour(num, nums_left)
        
def twentyfour(current_result, nums_left):
    global ans
    if len(nums_left) == 0: # if we've run out of numbers
        if ans == None and current_result <= 24: # if we haven't reached the answer at all, and our current result is less than 24
            ans = current_result
        elif current_result <= 24 and current_result > ans: # if we've found one solution, check if our current result is better, if so, update our answer
            ans = current_result
        return
    
    # brute force every single operation with every single remaining number to get all possibilities
    for num in nums_left:
        updated_nums_left = nums_left[:]
        updated_nums_left.remove(num)
        twentyfour(current_result + num, updated_nums_left)
        twentyfour(current_result - num, updated_nums_left) # subtraction is done twice as a - b != b - a
        twentyfour(num - current_result, updated_nums_left)
        twentyfour(current_result * num, updated_nums_left)
        if num != 0 and current_result % num == 0:
            twentyfour(current_result // num, updated_nums_left)
        if current_result != 0 and num % current_result == 0:
            twentyfour(num // current_result, updated_nums_left)
    if len(nums_left) == 2: # if we have two numbers left, try the results that would group those together ex: (a - b) * (c - d)
        twentyfour(current_result, [nums_left[0] + nums_left[1]])
        twentyfour(current_result, [nums_left[0] - nums_left[1]])
        twentyfour(current_result, [nums_left[1] - nums_left[0]])
        twentyfour(current_result, [nums_left[0] * nums_left[1]])
        if nums_left[0] % nums_left[1] == 0 and nums_left[1] != 0:
            twentyfour(current_result, [nums_left[0] // nums_left[1]])
        if nums_left[1] % nums_left[0] == 0 and nums_left[0] != 0:
            twentyfour(current_result, [nums_left[1] // nums_left[0]])

n = int(input())
computed = dict() # store previous answers in a dictionary to speed up process as there are duplicates
for _ in range(n): # get inputs
    ans = None
    inputs = []
    for _ in range(4):
        inputs.append(int(input()))
    inputs.sort()
    
    # if we've already computed the answer for this set of numbers, just use it again
    if tuple(inputs) in computed.keys():
        print(computed[tuple(inputs)])
        continue
    
    begin_solving(inputs)
    print(ans)
    computed[tuple(inputs)] = ans # store our answers