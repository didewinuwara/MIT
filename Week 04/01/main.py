# find the maximum mark related to 10 students

def findMax(markList):
    maximum=markList[0]
    markList.pop(0)
    for i in markList:
        if maximum<i:
            maximum=i
    print(maximum)

count=0
markList=[]
while count<10:
    mark=float(input("Enter Marks :"))
    markList.append(mark)
    count+=1
findMax(markList)
#otherwise we can use max function 