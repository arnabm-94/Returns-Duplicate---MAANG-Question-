'''
#Problem Statement 

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example :

Input: nums = [1,2,3,1]
Output: true
Hint: Use sets

'''

#Solution : 1


#Crate a function "contains_duplicate"
def contains_duplicate(nums):

#Create an empty set seen to store the unique elements encountered in the input array nums.
    seen = set()

#Iterate through the elements of nums using a for loop.
    for num in nums:
#For each element num in nums, check if it is present in the set seen.
        if num in seen: 
#If num is already in seen, that means it appears at least twice in the array. Return True.
            return True
#If the loop completes without finding any duplicates, add the current num to the set seen.
        seen.add(num)
#If the entire loop completes without finding any duplicates, return False.
    return False

# Example usage:
nums = [1, 2, 3, 1]
print(contains_duplicate(nums))  # Output: true

#===========================================

'''
#Time complexity:

Initialize an empty set called seen. The time complexity of this operation is O(1).

Start a for loop that iterates through each element in the input array nums. The loop will run n times, where n is the length of the input array.

Inside the loop, check if the current element num is already in the seen set. The average time complexity for this operation is O(1).

If the current element num is in the seen set, return True. This operation has a time complexity of O(1).

If the current element num is not in the seen set, add num to the seen set. The average time complexity for this operation is O(1).

After the loop is finished, if no duplicates were found, return False. This operation has a time complexity of O(1).

Since the loop runs n times and all operations inside the loop are constant time, the overall time complexity of the contains_duplicate function is O(n), where n is the length of the input array nums.

#Space Complexity:

O(n), where n is the length of the input array nums, as in the worst case, the set seen may store all unique elements of the array.


'''
