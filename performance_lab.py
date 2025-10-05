# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    frequency = dict()

    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    return max(frequency, key=frequency.get)

# print(most_frequent([1, 3, 2, 3, 4, 1, 3]))

"""
Time and Space Analysis for problem 1:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach?
    Using a dictionary for this gives us constant time for inserting and looking values up,
    so creating a frequency table is most efficient.
- Could it be optimized?
    I believe this is the most optimal it could be, besides any very small possible improvements.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    no_dupes = list()
    nums_set = set()

    for num in nums:
        if num not in nums_set:
            nums_set.add(num)
            no_dupes.append(num)
    
    return no_dupes

# print(remove_duplicates([4, 5, 4, 6, 5, 7]))

"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach?
    Using a set allows the ability to track already seen values.
    Using a list allows order to be maintained.
- Could it be optimized?
    I believe this is the most optimal it could be, besides any very small possible improvements.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    target_pairs = list()

    for num in nums:
        comp = target - num
        if comp not in seen:
            target_pairs.append(tuple(sorted((num, comp))))
        seen.add(num)
    
    return list(target_pairs)

# print(find_pairs([1, 2, 3, 4], 5))

"""
Time and Space Analysis for problem 3:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach?
    Using a set to track already seen numbers avoids using nested loops and prevents duplicates.
- Could it be optimized?
    I believe this is the most optimal it could be, besides any very small possible improvements.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    length = 0
    lst = [None] * capacity

    for i in range(n):
        if length == capacity:
            print(f'Resizing from capacity {capacity} to {capacity * 2}')
            capacity *= 2
            new_lst = [None] * capacity
            for j in range(length):
                new_lst[j] = lst[j]
            lst = new_lst
        lst[length] = i
        length += 1

# add_n_items(6)

"""
Time and Space Analysis for problem 4:
- When do resizes happen?
    Resizes happen when the number of items equals the current capacity.
- What is the worst-case for a single append? O(n)
- What is the amortized time per append overall? O(1)
- Space complexity: O(n)
- Why does doubling reduce the cost overall?
    It minimizes the amount of times the list needs to be resized.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = list()
    total = 0

    for num in nums:
        total += num
        result.append(total)

    return result

# print(running_total([1, 2, 3, 4]))

"""
Time and Space Analysis for problem 5:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach?
    It is a very simple and easy approach to the problem, avoiding nested loops or recalculations.
- Could it be optimized?
    If we were allowed to modify the list given, the space complexity could be optimized a bit more.
"""


# 🔍 Problem 5 (Optimized): Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    return nums

# print(running_total([1, 2, 3, 4]))

'''
The time complexity of the original version and the refactored version remains the same,
however, since we are modifying the given list in place, we do not have the need to
make a second list for the output. This changes the space complexity from O(n) to O(1).
'''