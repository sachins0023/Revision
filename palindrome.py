def check_palindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

sample_string = "malayalam"
isPalindrome = check_palindrome(sample_string.lower())
if isPalindrome == True:
    print("Entered string is a palindrome")
else:
    print("Entered string is not a palindrome")