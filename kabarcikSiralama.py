def bublesort(dizi):
    uzunluk=len(dizi)
    for i in range(uzunluk):
        for j in range(0,uzunluk-i-1):
            if dizi[j]>dizi[j+1]:
                dizi[j],dizi[j+1]=dizi[j+1],dizi[j]
dizi=[64,34,25,12,22,11,90]
bublesort(dizi)
print dizi
