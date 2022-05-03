# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.



import math


def isPalidrome(x: int) -> bool:
    
    a = list(str(x))
    b = list(str(x))
    
    
    a.reverse()
    print('a', a)
    print('b', b)

    if a == b: 
        return True
    return False


def main(): 
    palidrome = isPalidrome(x = -121)
    print(palidrome)


if __name__ == '__main__':
    main()