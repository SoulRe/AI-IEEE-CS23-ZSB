import os
#global variable to count the zeros of each row
zero_count = []
def get_sub(manual_string):
    """
    Function to get the Subscript Number
    Input:
        number in String Format
    Output:
        number in subscript format
    
    """
    normal, sub_s = "0123456789", "₀₁₂₃₄₅₆₇₈₉"
    trans = manual_string.maketrans(normal, sub_s)
    return manual_string.translate(trans)


def get_normal(example_string):
    """
    Function to get the normal Number from a subscript input
    Input:
        number in subscript format
    Output:
        number in String Format
    
    """
    normal, sub_s = "0123456789", "₀₁₂₃₄₅₆₇₈₉"
    trans = example_string.maketrans(sub_s, normal)
    return example_string.translate(trans)


def get_numbers(string_equation):
    
    """
    Function to return the numbers in a string
    
    Parameters
    ----------
    string : String
        Inputed equation in a string format.

    Returns
    -------
    s : list
        a List containing The numbers in the inputed string(signed and float).

    """
    string_equation =string_equation.replace("x"," ")
    string_equation =string_equation.replace("- ","-")
    numbers_list = []
    for t in string_equation.split():
            try:
                numbers_list.append(float(t))
            except ValueError:
                pass
    return numbers_list


def get_list(listy, num_of_equations):
    """
    Function to return a list containing the Parameters of the eqution including
    missing variables and in a sorted(respective to the equation) format

    Parameters
    ----------
    listy : List
        2Dlist in which every list has the first element as the parameter and
        the second element as the index of X.
    num_of_equations : int
        Number of equations .

    Returns
    -------
    elements : List
        containing the Parameters of the eqution including
        missing variables and in a sorted(respective to the equation) format.

    """
    elements = []
    indecies = list(range(1,num_of_equations+1))
    inputedIndecies = []
    for i in range(0, len(listy)-1, 2):
        inputedIndecies.append(listy[i+1])
        elements.append([listy[i], listy[i+1]])
    indecies = list(set(indecies) - set(inputedIndecies))
    
    global zero_count
    zero_count.append(len(indecies))
    
    if(len(indecies)>0):
        for i in range(len(indecies)):
            elements.append([0.0,indecies[i]])
    elements.sort(key= lambda x:x[1])
    
    for i in range(len(elements)):
        elements[i] = elements[i][0]
    elements.append(listy[len(listy)-1])
    return elements


def swap_rows(matrix, zero_count, num_of_equations):
    """
    

    Parameters
    ----------
    matrix : 2D List
        containing equations as Rows.
    zero_count : List
        contains the zeros of each row.
    num_of_equations : int
        number of equations.

    Returns
    -------
    matrix : 2D List
        matrix with the zeros in the end of the matrix.

    """
    for i in range(num_of_equations - 1):
        for j in range(i+1, num_of_equations):
            if zero_count[i] > zero_count[j]:
                
                zero_count[i], zero_count[j] = zero_count[j], zero_count[i]
                matrix[i], matrix[j] = matrix[j], matrix[i]
                
    return matrix

def getting_equations():
    """
    Function to get the inputed equations from equations.txt file

    Returns
    -------
    info : List
        2D list acts as the augmented matrix .

    """
    try:
        open('equations.txt', 'r')
    except FileNotFoundError:
        print("equations.txt doesn't exist")
        
    with open('equations.txt', 'r', encoding= 'utf-8') as file:
        info = []
        for line in file:
            info.append(line.strip('\n'))
    
    num_of_equations = int(info[0].split()[3])
    info.pop(0)
    
    for i in range(0, num_of_equations):
        info[i] = get_list(get_numbers(get_normal(info[i])), num_of_equations)
    
    # print(info)
    return info


def examples(elements):
    """
    Function to write the Guide to the user_manual.txt file

    Parameters
    ----------
    elements : int
        Number of equations.

    Returns
    -------
    None.

    """
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
            
            examp.write(get_sub(string)+'\n')



    
    
   
def main():
    #user_maunual.txt part
    while True:
        try:
            elements = int(input("Enter Number of equations: "))
            break
        except ValueError:
            print("Please enter a number!")
        
    examples(elements)
    print("\nUser Manual: "+os.path.abspath('user_manual.txt')+"\n")
    #examples.txt part
    matrix = getting_equations()
    matrix = swap_rows(matrix, zero_count, elements)
    return matrix

    
# main()
