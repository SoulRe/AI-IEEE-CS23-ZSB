class Solution:
    def isPalindrome(self, s: str) -> bool:
        #lower casing the input and saving in a string value for easier coding
        string = s.lower()

        #looping through each character and replacing it if not alphanumeric
        for i in string:
            if i.isalnum() == False:
                string = string.replace(i, "")

        #checking if the string is a palindrome and returning true if is
        if string == string[::-1]:
            return True

        #returning false by default if not a palindrome
        return False
        