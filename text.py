data = [50,2,16,1,0,900, 4]


def min(data: list, count=0, changed=False):
    if (data[count]>data[count+1]):
        data[count], data[count+1] = data[count+1], data[count]
        changed = True

    count+=1
    if (count==len(data)-1):
        count = 0
        
        if (changed==False):
            return data[0]
        
        changed = False

    return min(data, count, changed)

print(min(data))