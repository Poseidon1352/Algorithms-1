def count_and_sort(arr):
    if len(arr) == 1:
        return arr,0
    else:
        split_point = round(len(arr)/2);
        (Larr,nLi) = count_and_sort(arr[0:split_point])
        (Rarr,nRi) = count_and_sort(arr[split_point:])
        (Sarr,nSi) = count_and_merge(Larr,Rarr)
        return Sarr,nLi+nSi+nRi

def count_and_merge(Larr,Rarr):
    nSi = 0; size_L = len(Larr); size_R = len(Rarr);
    i = 0; j = 0; Sarr = [];
    for k in range(0,size_L+size_R):
        if j == size_R or (i < size_L and Larr[i] <= Rarr[j]):
            Sarr.append(Larr[i])
            i = i + 1
        else:
            Sarr.append(Rarr[j])
            nSi = nSi + size_L - i;
            j = j + 1
    return Sarr,nSi
    
file = open('IntegerArray.txt','r')
arr = []
for i in range(0,100000):
    arr.append(int(file.readline()))
(_,nInv) = count_and_sort(arr)
print(nInv)