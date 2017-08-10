def bubbleSort(array):
    uzunluk=len(array)
    for i in range(uzunluk):
        for j in range(0,uzunluk-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
array=[64,34,25,12,22,11,90]
bubbleSort(array)
print array
