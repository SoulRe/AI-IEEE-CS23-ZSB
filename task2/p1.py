"""function that sorts the list in ascending order"""
def sort_list(user_input, length):
    switch = 0
    for i in range(length):
        for j in range(i+1, length):
            if user_input[j] < user_input[i]:
                switch = user_input[j]
                user_input[j] = user_input[i]
                user_input[i] = switch
    return user_input
         
"""function that finds the first appearance in the list and the last"""
def find_appearances(user_input, length, target):
       for i in range(length):
           if user_input[i] == target:
               print(i, end = " ")
               break
        
       for i in reversed(range(length)):
           if user_input[i] == target:
                print(i)
                break
           
"""main function where input is taken and functions are called"""
def main():
    user_input = list(map(int, input("Input: \n").split()))
    length = len(user_input)
    target = int(input())
    user_input = sort_list(user_input, length)
    print(user_input)
    find_appearances(user_input, length, target)
    
main()
            
    
    