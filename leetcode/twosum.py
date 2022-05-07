# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]





from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    
    # n = len(nums)
    
    # for i in range(n): 
    #     print('outerloop', i)
    #     for j in range(1, n):
    #         print('innter loop:', j)
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    # Using hash or enumerate. 
    hash = {}
    for index, value in enumerate(nums):
        print(index, value)
        match = target - value
        if match in hash: 
            return [hash[match], index]
        hash[value] = index

def main():
    nums = [3,3]
    target = 6
    soulution = twoSum(nums, target)
    print('solution: ', soulution)


if __name__ == '__main__':
    main()