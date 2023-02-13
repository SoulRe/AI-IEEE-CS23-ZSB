import getting_info, os


def gauss_jordan_elimination(matrix, elements):
    ##zeroing down Lower triangle
    for i in range(elements):
        for j in range(0, i):
            element1, element2 = matrix[j][j], matrix[i][j]
            for m in range(elements + 1):
                matrix[i][m] = element2*matrix[j][m] - element1*matrix[i][m]
                
    ##zeroing down Upper triangle            
    for i in range(elements):
        if i < elements - 1:    
            for k in range(i+1, elements):
                element1, element2 = matrix[i][k], matrix[k][k]
                for n in range(elements + 1):
                    matrix[i][n] = element2*matrix[i][n] - element1*matrix[k][n]
                    
    ##inserting the solution into values list
    ##and checking the type of solution
    values = []
    solution="There is one solution:\n\n"
    for i in range(elements):
        if matrix[i][i] not in [0.0, -0.0]:
            if matrix[i][elements] in [0.0, -0.0]:
                values.append(matrix[i][elements])
                continue
            values.append(matrix[i][elements]/matrix[i][i])
            
        else:
            #if the all the elements in a row equals zero
            #and the result of that row is zero then its INFINITE SOLUTION Type
            if matrix[i][elements] in [0.0, -0.0]:
                solution="INFINITE SOLUTION"
                break
            else:
                #if the all the elements in a row equals zero
                #and the result of that row is Nonzero then its NO SOLUTION Type
                solution = "NO SOLUTION"
                break
            
    if(len(values)>0):    
        for i in range(elements):
            temp ='X{} = %0.2f' %(values[i])
            solution+=temp.format(getting_info.get_sub(str(i+1)))
            solution+= "\n"
    return solution
        
    
def main():
    try:
        matrix = getting_info.main()
        elements = len(matrix)
    except FileNotFoundError:
        print("Make sure equations.txt is created..")
        return
    
    return_value = gauss_jordan_elimination(matrix,elements)
    
    print("Solution File: "+os.path.abspath('solution.txt')+"\n")
    
    with open('solution.txt', 'w', encoding='utf-8') as solution:
        
        solution.write(return_value+"\n\n\n\n\n\n\n\n\n\n\n")
        solution.write("-------------\               -----------------  \n")
        solution.write("|             \              |\n")
        solution.write("|              \             |\n")
        solution.write("|              |             |\n")
        solution.write("|              |             |\n")
        solution.write("|              |             |---------------\n")
        solution.write("|              |             |\n")
        solution.write("|              /             |\n")
        solution.write("|             /              |\n")
        solution.write("-------------/               ----------------\n")
        
        
main()
