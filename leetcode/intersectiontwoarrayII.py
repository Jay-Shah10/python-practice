"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


Example 1: 
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2: 
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""


def solution(nums1, nums2):
    mapping = {}
    result = []

    for numi in nums1:
        if numi in mapping: 
            mapping[numi] += 1
        else: 
            mapping[numi] = 1
    
    for numj in nums2: 
        if numj in mapping and mapping[numj] > 0: 
            result.append(numj)
            mapping[numj] -= 1
    
    return result

def solution2(nums1, nums2): 
    # not the best solution: Time complixy is going to be O(n)

    result = []
    for i in nums1: 
        if i in nums2: 
            result.append(i)
    return result
    

def main(): 
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]

    print("solution 1:", solution(nums1, nums2))
    print("solution 2:", solution2(nums1, nums2))

if __name__ == '__main__':
    main()