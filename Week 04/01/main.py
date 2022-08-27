# find the maximum mark related to 10 students

def findMax(markList):
    maximum=markList[0]
    markList.pop(0)
    for i in markList:
        if maximum<i:
            maximum=i
    print(maximum)

markList=[]
for count in range(10):
    mark=float(input("Enter Marks :"))
    markList.append(mark)
findMax(markList)
#otherwise we can use max function 