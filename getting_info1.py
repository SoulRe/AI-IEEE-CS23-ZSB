import os


def get_sub(x):
    normal, sub_s = "0123456789", "₀₁₂₃₄₅₆₇₈₉"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)


def get_normal(x):
    normal, sub_s = "0123456789", "₀₁₂₃₄₅₆₇₈₉"
    res = x.maketrans(''.join(sub_s), ''.join(normal))
    return x.translate(res)


def get_numbers(string):
    string =string.replace("x"," ")
    string =string.replace("- ","-")
    s = []
    for t in string.split():
            try:
                s.append(float(t))
            except ValueError:
                pass
    return s


def get_list(listy, num_of_equations):
    elements = []
    for i in range(0, len(listy)-1, 2):
        # if i == len(listy)-2:
        #     elements.append(float(listy[i]))
        #     break
        elements.append([listy[i], listy[i+1]])
    elements.sort(key= lambda x:x[1])
    
    for i in range(len(elements)):
        elements[i] = elements[i][0]
    elements.append(listy[num_of_equations - 1])
    return elements


def getting_equations():
    try:
        open('equations.txt', 'r')
    except FileNotFoundError:
        print("File doesn't exist")
        return
    with open('equations.txt', 'r', encoding= 'utf-8') as file:
        info = []
        for line in file:
            info.append(line.strip('\n'))
    
    num_of_equations = int(info[0].split()[3])
    info.pop(0)
    
    for i in range(0, num_of_equations):
        info[i] = get_list(get_numbers(get_normal(info[i])), num_of_equations)
            
    print(info)
    return info


def examples(elements):
    with open('user_manual.txt', 'w', encoding= "utf-8") as examp:
        examp.write("This file is your catalogue to use this program.\n\n\
First, Store your equations in a text file named 'equations.txt'.\n\n\
If you have {} equations, Your text file should be like this:\n\n\
Number of equations: {}\n\n".format(elements, elements))
        
        for i in range(elements):
            string = "eq{}: "
            for j in range(elements):
                var = "a{}{}x{} + "
                var = var.format(i+1, j+1, j+1)
                string = string + var
                
            string = string[:-2]
            string += "= a{}0"
            string = string.format(i+1, i+1)
            # string = get_sub(string)
            examp.write(get_sub(string)+'\n')


# def getting_equations():
    
    
   
def main():
    #user_maunual.txt part
    # try:
    #     elements = int(input("Enter Number of equations: "))
    # except ValueError:
    #     print("Please enter a number!")
        
    # examples(elements)
    # print("\n"+os.path.abspath('user_manual.txt'))
    
    #examples.txt part
    matrix = getting_equations()
    
    
main()
