def maxmin(data):
    if len(data)==1:
        return data[0],data[0]
    else:
        max = min = data[0]
        for i in range(1,len(data)):
            if max < data[i]:
                max = data[i]
            if min > data[i]:
                min = data[i]
        return max,min

if __name__ =="__main__":
    l1 = [1]
    l2 =[65,34,1324,45,34,723,45,234,567,234,4567]
    print(maxmin(l1))
    print(maxmin(l2))