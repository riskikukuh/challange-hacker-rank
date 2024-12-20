def sockMerchant(n, ar):
    result = 0
    temp = []
    for x in range(n):
        try:
            tempIndex = temp.index(ar[x])
            temp.pop(tempIndex)
            result += 1
        except:
            temp.append(ar[x])
    return result

data = [10, 20, 20, 10, 10, 30, 50, 10, 20]
sockMerchant(len(data), data)