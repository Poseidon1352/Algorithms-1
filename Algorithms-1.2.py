from statistics import median

def quick_sort(arr):
    return partition(arr,0,len(arr)-1)
    
def partition(arr,l,r):
    if l < r:
        #Case 1
        #pivot = arr[l]
        #Case 2
        #pivot = arr[r]
        #arr[r] = arr[l]
        #Case 3
        pivot = median([arr[l],arr[int((l+r)/2)],arr[r]])
        if pivot == arr[r]:
            arr[r] = arr[l]
        elif pivot == arr[int((l+r)/2)]:
            arr[int((l+r)/2)] = arr[l]
        i = l
        for j in range(l+1,r+1):
            if arr[j] < pivot:
                i = i + 1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        arr[l] = arr[i]
        arr[i] = pivot
        return partition(arr,l,i-1) + partition(arr,i+1,r) + r - l
    else:
        return 0

file = open('QuickSort.txt','r')
arr = []
for i in range(0,10000):
    arr.append(int(file.readline()))
print(quick_sort(arr))