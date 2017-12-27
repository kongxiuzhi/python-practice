def power1(x,n):
    if n==0:
        return 1
    return x.power1(x,n-1)

def power2(x,n):
    if n==0:
        return 1
    else:
        result = power2(x,n//2)
        result = result*result
        if n%2 == 0:
            result *= x
        return result

