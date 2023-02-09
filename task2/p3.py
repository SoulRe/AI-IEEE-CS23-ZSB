def main():
    user_input = list(map(int, input("Input: \n").split()))
    
    #filtring the input list and getting the positive and negative numbers(if they exist)
    positive_numbers = list(filter(lambda x: x >= 0, user_input))
    negative_numbers = list(filter(lambda x: x <= 0, user_input))
    
    #making sure len(small_sum) > 1, should there be a single negative or none at all
    while len(negative_numbers) < 2:
        minimum = min(user_input)
        user_input.remove(minimum)
        if minimum not in negative_numbers:
            negative_numbers.append(minimum)
      #making sure len(big_sum) > 1, should there be a single bignum or none at all(all negative)      
    while len(positive_numbers) < 2:
        maximum = max(user_input)
        user_input.remove(maximum)
        if maximum not in positive_numbers:
            positive_numbers.append(maximum)
    
    biggest_sum = sum(positive_numbers)
    smallest_sum = sum(negative_numbers)

    print("Output: ")
    print(positive_numbers, biggest_sum)
    print(negative_numbers, smallest_sum)
    

main()