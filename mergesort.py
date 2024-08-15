import random as rd

def mergeSort(L, first, last):
    if last >= first:
        return
    # recursive case : first < last, i.e, list contains at least 2 elements
    mid = (first + last) // 2
    #conquer step 1: sort(first.. mid - 1]
    mergeSort(L, first, mid)
    # conquer step 2: sort L[mid, last
    mergeSort(L, mid + 1, last)

    # this is a whole dif function?
    merge(L, first, mid, last)

def merge(L, first, mid, last):
    i = first
    j = mid + 1
    temp = []
    while (i <= mid) and (j<= last):
        if L[i] <= L[j]:
            temp.append(L[i])
            i += 1
        else:
            temp.append(L[j])
            j += 1
    if i > mid:
        temp.extend(L[j:last + 1])
    elif j > last:
        temp.extend(L[i:mid + 1])
    L[first:last+1] = temp

L = [4, 7, 8, 12, 21, 30, 31, 31, 1, 5, 9]
new_L = merge(L, 0, 7, 10)
# print(new_L)


# x = [1,5,6,7,0]
# print(len(x))
# print(list(range(len(x))))





rawRatings = [(1,1,1) * 2]
list_of_possible_indexes = list(range(len(rawRatings)))
testPercent = 20 / 100
len_of_testSet = int(len(rawRatings) * testPercent)

def testing():
    rawRatings = [(1, 1, 1) * 2]
    list_of_possible_indexes = list(range(len(rawRatings)))
    print(list_of_possible_indexes)
    testPercent = 20 / 100
    len_of_testSet = int(len(rawRatings) * testPercent)
    i = 0
    for i in range(0,len_of_testSet):
        print("hi")
        i += 1



testSet = []
test_percent = 20 / 100
rawRatings = [(1,1,1),(2,2,2),(3,3,3), (4,4,4),(5,5,5),(6,6,6),(7,7,7),(8,8,8),(9,9,9),(10,10,10)]
indexes = list(range(len(rawRatings)))
lenOfTestSet = round(len(rawRatings) * test_percent)


for i in range(0,2):
    pickedIndex = rd.choice(indexes)
    testSet.append(rawRatings[pickedIndex])
    indexes.remove(pickedIndex)

print(testSet)

trainingSet = [rawRatings[i] for i in indexes]
print(trainingSet)



s = [1,2,3]
y = [4,5,6]
print([s,y])