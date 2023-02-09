from p4 import user_data as users

def main():
    string = []
    with open('filtered.txt', 'w') as file:
        for i in users.keys():
            file.write("{} {} - {}\n".format(i, users[i]['name'], users[i]['birth']))
    print("Filtering Done!")
            
main()