s = "Shivam"

def reverse_string(s):
    s = list(s)
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left],s[right] = s[right],s[left]
        left += 1
        right -= 1
        
    return ''.join(s)    

print(reverse_string(s))

# Time complexity is O(n), where n is the length of the string.
# Space complexity is O(n), because we convert the sting to a list.