"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

------

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longestCommonPrefix(strs):
    if not strs:
        return ""
    for i, letter_value in enumerate(zip(*strs)):
        # print(i)  # returns the index
        # returns a list of [(0, 'flower'), (1, 'flow'), (2, 'flight')]
        # print(letter_value) # returns the value
        if len(set(letter_value)) > 1:
            return strs[0][:i]
    else:
        return min(strs)

if __name__ == '__main__': 

    strs = ['flower', 'flow', 'flight']
    result = longestCommonPrefix(strs)
    print(result)
