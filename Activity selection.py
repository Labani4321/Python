##Activity Selection problem
def printMaxActivities(s, f):
    n = len(f)
    print ("Following activities are selected")
    i = 0
    print (i)
    for j in range(1, n):
        if s[j] >= f[i]:
            print (j)
            i = j
            
# Driver code
if __name__ == '__main__':
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    printMaxActivities(s, f)

