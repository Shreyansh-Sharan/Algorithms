def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr [j]
            j-=1
        arr[j+1] = key
    return arr


if __name__ == "__main__":
    test = [21,3,23,43,1,35,2,55] 
    sortedArray = insertionSort(test)
    print(sortedArray)