import getting_info


def gauss_jordan_elimination(matrix, elements):
    for i in range(elements):
        for j in range(0, i):
            element1, element2 = matrix[j][j], matrix[i][j]
            for m in range(elements + 1):
                matrix[i][m] = element2*matrix[j][m] - element1*matrix[i][m]
                
                
    for i in range(elements):
        if i < elements - 1:    
            for k in range(i+1, elements):
                element1, element2 = matrix[i][k], matrix[k][k]
                for n in range(elements + 1):
                    matrix[i][n] = element2*matrix[i][n] - element1*matrix[k][n]
                    

    values = []
    solution="There is one solution:\n\n"
    for i in range(elements):
        if matrix[i][i] not in [0.0, -0.0]:
            if matrix[i][elements] in [0.0, -0.0]:
                values.append(matrix[i][elements])
                continue
            values.append(matrix[i][elements]/matrix[i][i])
            
        else:
            if matrix[i][elements] in [0.0, -0.0]:
                solution="INFINITE SOLUTION"
                break
            else:
                solution = "NO SOLUTION"
                break
            
    if(len(values)>0):    
        for i in range(elements):
            temp ='X{} = %0.2f' %(values[i])
            solution+=temp.format(getting_info1.get_sub(str(i)))
            solution+= "\n"
    return solution
        
    
def main():
    matrix = getting_info.main()
    elements = len(matrix)
    
    return_value = gauss_jordan_elimination(matrix,elements)
    
    with open('solution.txt', 'w', encoding='utf-8') as solution:
        solution.write(return_value+"\n\n\n\n\n\n\n\n\n\n\n")
        solution.write("-------------\              -----------------  \n")
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