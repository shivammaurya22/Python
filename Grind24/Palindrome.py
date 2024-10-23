# string isPalindrome question 

def is_palindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1 
        while left < right and not s[right].isalnum():
            right -= 1
        
        #comapre characters case insensitively
        if s[left].lower() != s[right].lower():
            return False        
        
        left += 1 
        right -= 1
    return True

s = "abba"
print(is_palindrome(s))
        
        