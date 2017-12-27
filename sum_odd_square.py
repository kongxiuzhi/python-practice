def sum_odd_square(n):
    if n <= 0:
        raise AttributeError("must be a positive number")
    sum = 0
    for j in range(n):
        if j%2 != 0:
            sum += j**2
    return sum

if __name__ =="__main__":
    s9 = sum_odd_square(9)
    print(s9)