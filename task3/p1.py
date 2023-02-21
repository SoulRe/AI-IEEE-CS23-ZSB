"""This program works on the assumption that the inputed list will have ints not floats
    it could work with floats if the mapped type is float instead of int"""

def get_input():
    """Getting input from the user and making sure it's at least 1 number
    &handling any error that might come from the user wanting to quit """
    while True:
        try:
            numbers_list = list(map(int, input("Input: \n").split()))
            while len(numbers_list) < 1:
                print("List must contain numbers!")
                numbers_list = list(map(int, input("Input: \n").split()))
            break
        except ValueError:
            print("Please enter an all int list")
        #should the user quit using keyboard interrupt a message is displayed telling them they quit
        except KeyboardInterrupt:
            print("Exited!")
            return
    #sorting the list to be used in the get_median function,it has no affect on other function
    numbers_list.sort()
    return numbers_list, len(numbers_list)


def get_mean(numbers_list, length):
    """function to get the mean of a list of numbers

    Args:
        numbers_list (list): the list entered by the user
        length (int): the length of the list the user entered

    Returns:
        mean: the calculated mean
    """
    mean = sum(numbers_list) / length
    return mean


def get_median(numbers_list, length):
    """a function to calculate the median of a list of numbers

    Args:
        numbers_list (list): list of numbers entered by the user
        length (int): length of user entered list

    Returns:
        median: the calculated median depending on whether the length was even or odd
    """
    median = 0
    if length %2 == 0:
        middle = length //2 - 1
        #adding the values of the middle 2 numbers of the list and dividing by 2
        median = (numbers_list[middle] + numbers_list[middle + 1])/2
        return median
    else:
        middle = length // 2
        median = numbers_list[middle]
        return median


def get_mode(numbers_list):
    """takes the list of numbers finds out which number is the most frequent
    
    INPUT: numbers_list : the list of ints the user entered
    OUTPUT: a print message in the case of each number appearing once
    OUTPUT: a list of numbers that are most frequent, len(list) >= 1"""
    
    #numbers is a set of all numbers that appeared in the list without duplicates
    sum_of_appearances, numbers, appearance_list = 0, set(numbers_list.copy()), []
    #looping through the numbers in the set and counting their appearance in the entered list
    #adding the [number, freq] to another list appearance_list
    for i in numbers:
        count = numbers_list.count(i)
        appearance_list.append([i, count])
        sum_of_appearances += count  
    #making another list which will contain the values to be returned
    return_list = []
    
    #checking if each number has appeared only once
    if sum_of_appearances == len(numbers):
        print("This list has no Mode")
        exit()
    
    #adding all the numbers that have the same freq as the most freq number to the return list and returning it
    else:
        appearance_list.sort(reverse = True, key = lambda x:x[1])
        for i in range(0, len(numbers)):
            if appearance_list[i][1] == appearance_list[0][1]:
                return_list.append(appearance_list[i][0])  
        return return_list
    
    
    
def main():
    try:
        numbers_list, length = get_input()
    except:
        return
    
    #printing the mean
    print("\nmean = %0.3f" % get_mean(numbers_list, length))
    
    #printing the median
    print("median = ",get_median(numbers_list, length))
    
    #printing the mode
    #checking if the list is multimodal or not
    mode_list = get_mode(numbers_list)
    if len(mode_list) > 1:
        print("This list is multimodal!")
        print("modes =", end = " ")
        
    #printing each number in the list
    for i in range(len(mode_list)):
        if i == len(mode_list) - 1:
            print(mode_list[i], end = " ")
            break
        print(int(mode_list[i]), end = ", ")
     
     
            
main()
