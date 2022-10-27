def bubbleSort(arr):
    swapped = False
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break   
    return arr 

if __name__ == "__main__":
    test = [1,2,4]
    sortedArray = bubbleSort(test)

    print(sortedArray)
