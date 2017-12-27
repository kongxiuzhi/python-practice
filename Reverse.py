def Reverse(S,start,stop):
    if start < stop-1:
        S[start],S[stop]=S[stop],S[start]
        Reverse(S,start+1,stop-1)

if __name__=="__main__":
    s1=[1,2,3,4,5,6,7,8,9,10]
    Reverse(s1,0,9)
    print(s1)