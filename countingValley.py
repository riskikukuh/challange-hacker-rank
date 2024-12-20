from curses.ascii import alt
import math

# Mark as Overengineering

# Best Solution
def countingValleys(steps, path):
    valleys = 0
    cur_level = 0
    for steps in path:
        if(steps == 'U'):
            cur_level += 1
            if(cur_level == 0):
                valleys += 1
        elif(steps == 'D'):
            cur_level -= 1
    return(valleys)

# MySolution to draw
def countingValleys(steps, path):
    # Write your code here
    topAltitude = 0 + path.count('U') - path.count('D')
    arr = [[" " for x in range(steps+2)] for y in range(steps+2)] 

    length = 1
    altitude = math.floor(steps/2)
    arr[altitude][0] = "_"
    for i, x in enumerate(path):
        prevStep = "" if i == 0 else path[i-1]
        value = "/" if x == "U" else '\\'
        
        if x == "U":
            if prevStep == "U":
                altitude -= 1
        else :
            if prevStep == "D":
                altitude += 1
        arr[altitude][length] = value
        
        length += 1

    if arr[altitude][length-1] == "/":
        arr[altitude-1][length] = "_"
    elif arr[altitude][length-1] == "\\":
        arr[altitude][length] = "_"

    for x in arr:
        temp = ""
        for i in x:
            temp+=i
        if temp != len(x)*" ":
            print(temp)

steps = 8
path = 'DDUUDDUDUUUD'
countingValleys(len(path), path)