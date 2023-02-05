def main():
    items = list(map(int, input("input: \n").split()))
    items.sort()
    print("output:")
    print(items[len(items) - 2])
    print(items[1])
    
    
main()