def get_input():
    """getting int based input from user and making sure we get atleast one number """
    while True:
        try:
            number_list = list(map(int, input("Input: \n").split()))
            while len(number_list) < 4:
                print("List must have at least 4 numbers!")
                number_list = list(map(int, input("Input: \n").split()))
            break
        except(ValueError):
            print("Please Enter an all int list")
        except(KeyboardInterrupt):
            print("Exit succesful")
            exit()
    
    number_list.sort()
    return number_list, len(number_list)


def get_median(num_list):
    """function to get the median of a list passed to the function"""
    median, list_length = 0,  len(num_list)
    mid_point = (list_length - 1) // 2
    
    if list_length % 2 == 0:
        median = (num_list[mid_point] + num_list[mid_point + 1]) / 2
    else:
        median = num_list[mid_point]
        
    return median, mid_point


def get_quartiles(numbers, length):
    """Function to get each of the quartiles using the function get median"""
    second_quartile, mid_point = get_median(numbers)
    
    #if the list length is even then we wanna stop at the value of the divison by 2
    if length % 2 == 0:
        first_quartile = get_median(numbers[0: (length // 2)])[0]
        third_quartile = get_median(numbers[(length // 2):])[0]
    #if the list is odd then we go to just before the index of the 2nd quartile and start from after it
    else:
        first_quartile = get_median(numbers[:mid_point])[0]
        third_quartile = get_median(numbers[mid_point + 1:])[0]
        
    inter_quartile_range = third_quartile - first_quartile
    
    return first_quartile, second_quartile, third_quartile, inter_quartile_range
    
    
def get_deviation(numbers, length):
    """function to calculate the variance and standard devition"""
    mean = sum(numbers)/length
    print(mean)
    variance = 0
    
    for i in range(length):
        variance += (numbers[i] - mean)**2
        
    variance /= length
    standard_deviation = variance**(0.5)
    
    return variance, standard_deviation
    

def main():
    numbers, length = get_input()
    
    first_quartile, second_quartile, third_quartile, inter_quartile_range = get_quartiles(numbers, length)
    variance, standard_deviation = get_deviation(numbers, length)
    
    #printing the output
    print("\nOutput:")
    print("Min : {}".format(numbers[0]))
    print("Q1: {}".format(first_quartile))
    print("Q2: {}".format(second_quartile))
    print("Q3: {}".format(third_quartile))
    print("Max : {}".format(numbers[length - 1]))
    print("Range: {}".format(numbers[length - 1] - numbers[0]))
    print("IQR: {}".format(inter_quartile_range))
    print("Variance: %0.3f" % variance)
    print("Standard Deviation: %0.3f" % standard_deviation)
    
    
    
    

main()