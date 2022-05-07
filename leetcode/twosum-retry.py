"""
Description: 
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1: 
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2: 
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3: 
Input: nums = [3,3], target = 6
Output: [0,1]

"""


def twoSum(nums, target):
    d = {}
    for i, v in enumerate(nums):
        match = target - v 
        if match in d: 
            return [d[match], i]
        else: 
            d[v] = i


def main(): 
    nums = [2,7,11,15]
    target = 9
    result = twoSum(nums, target)
    
    print('Result:', result)
    #expected outcome: [0,1]


if __name__ == '__main__':
    main()


"""
Explination: 

d = {}
    for i, v in enumerate(nums):
        match = target - v 
        if match in d: 
            return [d[match], i]
        else: 
            d[v] = i

This is using a hashmap or dict in python. 
we first define an empty dict --> d = {}

Then we are going to use enumerate in python which gives us access to index and value in a list. 
Then we are going to find a 'match'. since subtracting traget value with an index  and that we know we will have atleast
one solution, it is easier to keep track of this way. Plus we are going to be adding the values as keys in the dict and 
the index as values in dict. This way it will keep track of value's index. 

Example: 2 + 7 = 9  || 9 - 2 = 7 . 

Then we do a check for the match in d first.
We do this first because we will have to fill up the dict rather than stopping at if we find a match. 
Plus at this moment d is emtpy. This will also prevent us from using same index - we can't use the same index. 
Example if the target is 4. 4-2 is 2 and if the first value in nums is 2 then we would have the answer. 

else: 
    Here we are filling up the dict. 

here is an example of this from Neetcode: https://www.youtube.com/watch?v=KLlXCFG5TnA&t=12s


"""