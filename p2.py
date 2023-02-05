def main():
    list_to_check = list(map(int, input("input: \n").split()))
    elements = len(list_to_check)
    middle_element = elements // 2
    for i in range(middle_element):
        # print(list_to_check[i], list_to_check[elements - i - 1])
        if list_to_check[i] != list_to_check[elements - i - 1]:
            print("Not symmetric")
            exit(0)
    else:
        print("symmetric")
        
        
main()