def linear_sum(S,n):
    if n==0:
        return S[0]
    return S[n-1]+linear_sum(S,n-1)

if __name__=="__main__":
    l1 = [1,2,3,4,5,6,7,8,9]
    for i in range(4,10):
        print(linear_sum(l1,i))
