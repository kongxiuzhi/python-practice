def fibonacci1(n):
    if n <0:
        raise ValueError("can't be negative")
    if n==0 or n==1:
        return 1
    a=b=1
    for i in range(n-1):
        a,b=b,a+b
    return b

def fibonacci2(n):
    if

if __name__=="__main__":
    for i in range(10):
        print(fibonacci1(i))

