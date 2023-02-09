#taking lines from file as raw_data
raw_data = []
with open('grades.txt') as data:
    for line in data:
        raw_data.append(line.split())

#adding all the user data that have scores and without the ":" and "-"
user_data = {}
average = 0
for i in range(1,len(raw_data)):
    """cleaning the raw data up and skipping anyone without a score."""
    raw_data[i].remove("-")
    raw_data[i].remove(":")
    if raw_data[i][2] == "N/A":
        continue
    
    """creating some variables to make it easier when making the dict"""
    ids, name, score, birth, gender = int(raw_data[i][0]) ,raw_data[i][1] ,int(raw_data[i][2]) ,int(raw_data[i][3]), raw_data[i][4]
    
    """getting the sum of all scores"""
    average += score
    
    """making the user_data dict and adding all the info into it."""
    current_user = dict(name = name, score = score, birth = birth, gender = gender)
    user_data[ids] = current_user

# print(user_data[ids]['gender'])
"getting the biggest score & the biggest age"
biggest_age = min(zip((k['birth'] for k in user_data.values()), user_data.keys()))[1]               #the k for k in user_data.values is a help from stackoverflow
biggest_score = max(zip((m['score'] for m in user_data.values()), user_data.keys()))[1]              # i didn't know how to do it anyother way that's why

"""getting the average of all the scores"""
average /= len(user_data)

"""answering the questions."""
if __name__ == '__main__':
    print("The ID of the oldest is:", biggest_age)
    print("The Gender of the highest scorer is:", user_data[biggest_score]['gender'])
    print("The Average score is: %0.2f"%average)
