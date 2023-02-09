def main():
    user_input = list(map(int, input("Input: \n").split()))
    even_numbers = list(filter(lambda x: x%2 == 0, user_input))
    print(len(even_numbers))


main()