# CPE 446 Lab 2
# ABFT (Matrix Multiplication)

# A x B = C - all lists of lists
def mat_mul(A, B):
    b = list(zip(*B))

    return [[sum(x*y for x,y in zip(row, col)) for col in b] for row in A]

# Matrix multiplication with Algorithmic Based Fault Tolerance (ABFT)
def abft_mat_mul(A, B):
    return null

asdf = [[1,2,3],[4,5,6],[7,8,9]]
zxcv = [[1,2],[3,4],[5,6]]

if __name__ == '__main__':
    print(mat_mul(asdf, zxcv))
