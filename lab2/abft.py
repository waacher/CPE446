# CPE 446 Lab 2
# ABFT (Matrix Multiplication)

# A x B = C - all lists of lists
def mat_mul(A, B):
    b = list(zip(*B))

    return [[sum(x*y for x,y in zip(row, col)) for col in b] for row in A]

# Matrix multiplication with Algorithmic Based Fault Tolerance (ABFT)
# Assumes checksums are correct
def abft_mat_mul(A, B):

    res = mat_mul(A,B)
<<<<<<< HEAD
    # For testing errors
    # res = [[30,36,42], [66,81,96], [103,126,150]]
=======
    # Insert errors here for testing 
    # res = [[30,36,42], [66,81,96], [102,126,150]]
>>>>>>> 519d15112fa850067091b73ce17d673211ca82da

    mat_checksum(A)
    mat_checksum(B)

    row_sums = [row[-1] for row in mat_mul(A[:-1], B[:-1])]
    col_sums = mat_mul(A, B)[-1][:-1]

    row_errors = []
    col_errors = []

    for i in range(len(res)):
        if (sum(res[i]) != row_sums[i]):
            row_errors.append(i+1)

    for i in range(len(res[0])):
        column = [row[i] for row in res]
        if (sum(column) != col_sums[i]):
            col_errors.append(i+1)
    
    if (len(row_errors) + len(col_errors) == 0):
        return res
    elif (len(row_errors) != len(col_errors)):
        print("Cannot detect error(s) (either checksums or multiplication)")
    elif (len(row_errors) == 1):
        print("Possible error in row " + str(row_errors[0]) + " col " + str(col_errors[0]))
    else:
        print("Multiple errors detected: cannot guarantee validity of computation")

    return res

# Generate row and col checkums for a matrix
def mat_checksum(mat):
    checksums = []
    for row in mat:
        row.append(sum(row))
    checksums.clear()
    for index in range(len(mat[0])-1):
        col_sum = 0;
        for j in range(len(mat)):
            col_sum+= mat[j][index]
        checksums.append(col_sum)
    # unused corner value
    checksums.append(0)
    mat.append(checksums)

def print_matrix(mat):
    for row in mat:
        print(row)

asdf = [[1,2,3],[4,5,6],[7,8,9]]
zxcv = [[1,2,3],[4,5,6],[7,8,9]]

if __name__ == '__main__':
    print_matrix(asdf)
    print("*")
    print_matrix(zxcv)
    print("||")
    matrix = abft_mat_mul(asdf, zxcv)
    print_matrix(matrix)
