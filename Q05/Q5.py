# this code is for python versions 3.x

x = int(input("Enter number of row for the pattern : "))
i = 0
while i <= x:
    for j in range(i):
        print("", end = " ")
    for j in range((x-i)*2-1):
        print('*', end ="") # for python 2.7.x write print('*'),
    print("")
    i+=1