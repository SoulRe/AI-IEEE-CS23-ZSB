def main():
    #taking in input and splitting each user's data
    user_input = list(map(str, input("input: \n").split(',')))
    final_list = []
    info_dict = {}
    #splitting each of the users data into a name and age 
    for i in range(len(user_input)):
        final_list.append(user_input[i].split(":"))
    #updating the dictionary
    for i in range(len(final_list)):
        info_dict.update({final_list[i][0]:final_list[i][1]})
    print("output: ")
    print(info_dict)

main()