def main():
    numbers = list(map(int, input("Input: \n").split()))
    rotations = int(input())
    newlist = []
    for i in range(len(numbers) - rotations, len(numbers)):
        newlist.append(numbers[i])
    for i in range(len(numbers) - rotations):
        newlist.append(numbers[i])
    print("Output: ")
    print(newlist)
    
    
main()
    