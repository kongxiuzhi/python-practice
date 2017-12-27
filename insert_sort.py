def insert_sort(A):

    for i in range(1,len(A)):
        temp = A[i]
        j=i-1
        while j >= 0 and temp > A[j]:
             A[j+1]=A[j]
             A[j] = temp
             j-=1

if __name__=="__main__":
    A = [1,2,3,4,5,7]
    insert_sort(A)
    print(A)

