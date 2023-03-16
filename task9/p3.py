class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        for i in range(len(emails)):
            x = 0
            #lowercasing the email
            emails[i] = emails[i].lower()
            
            #getting the starting point of the domain
            at_sign = emails[i].index('@')

            #Saving the domain address
            domain = emails[i][at_sign: ]

            #ignoring dots in addressname
            address = emails[i][0: at_sign].replace(".", "")

            #checking if a + exists and ignoring the following
            x = address.find('+')
            if x != -1:
                address = address[:x]

            #saving the actual email in the emails list
            emails[i] = address + domain
        

        return len(set(emails))
