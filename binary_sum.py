def binary_sum(S,start,stop):
    if start > stop:
        return 0
    if start == stop-1:
        return S[start]
    mid = (stop+start)//2
    return binary_sum(S,start,mid)+binary_sum(S,mid,stop)

if __name__ =="__main__":
    S=[1,2,3,4,5,6,7]
    print(binary_sum(S,0,7))