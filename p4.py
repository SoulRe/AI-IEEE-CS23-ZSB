def main():
    numbers = list(map(int, input("Input: \n").split()))
    target_number = int(input())
    
    numbers_to_check = []
    for i in range(len(numbers)):
        if numbers[i] <= target_number:
            numbers_to_check.append([numbers[i], i])
            
    for i in range(len(numbers_to_check) - 1):
        for j in range(i, len(numbers_to_check)):
            if numbers_to_check[i][0] + numbers_to_check[j][0] == target_number:
                print(f"{numbers_to_check[i][1]}, {numbers_to_check[j][1]}")
                exit(0)
    else:
        print("No combination of numbers lead to target!")
        exit(0)
        

main()