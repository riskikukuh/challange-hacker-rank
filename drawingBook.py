# Mark as Overengineering

from unittest import result
import math

# My Solution
def pageCount(n, p):
    # Write your code here
    resultForward = -1
    for x in range(1, n+1):
        if x == p:
            resultForward = x/2

    resultForward = abs(math.floor(resultForward))

    lastPage = -1
    i = 0
    newLen = n
    if n % 2 == 0:
        lastPage = n
        newLen = n - 1
    if lastPage == p:
        return 0
    resultForward = find(newLen, p, True)
    resultBackward = find(newLen, p, False)
    
    if resultForward > resultBackward:
        if lastPage > 0:
            return resultBackward + 1
        else:
            return resultBackward
    else:
        return resultForward

def find(n, p, isForward):
    result = 0
    i=0
    for x in range(0 if isForward else n-1, -1 if not(isForward) else n, 2 if isForward else -2):
        firstData = x
        secondData = x + 1
        if firstData == p or secondData == p:
            result = i
        i+=1
    return result

# Solution on Internet
def solution(n, p):
    page_in_book = p//2
    total_pages = n//2

    from_front = page_in_book
    from_back = total_pages - page_in_book
    print(min(from_front,from_back))

n = 6
p = 5
result = pageCount(n, p)
print(result)