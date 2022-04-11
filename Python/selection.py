def selection(arr):
    n = len(arr)
    i = 1
    for i in range(1,n):
        temp = arr[i]
        j = i - 1
        for j in range(i-1,0):
            if arr[i] > temp:
                