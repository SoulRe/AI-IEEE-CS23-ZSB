def main():
    input_string = list(map(str, input("Input: \n").split()))
    first_half, second_half = [], []
    #iterating over each word in list
    for i in range(len(input_string)):
        word = ""
        #getting the middle character of the list
        midpoint = len(input_string[i]) // 2
        #if the length of word is odd we add 1 to the midpoint identifier
        if (len(input_string[i]))%2 != 0:
            midpoint += 1
        #we add the characters of the word into a variable and store it in a list
        for j in range(midpoint):
            word += input_string[i][j]
        first_half.append(word)
        word = ""
        for k in range(midpoint, len(input_string[i])):
            word += input_string[i][k]
        second_half.append(word)
    print("Output: ")
    print(first_half, second_half)
            
main()