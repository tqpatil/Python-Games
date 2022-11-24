def list_comprehension(A):
    B= [A[x]+A[x+1] for x in range(len(A)-1)]
    return B

