def arayaEkleme(dizi):
    for i in range(1, len(dizi)):
        key = dizi[i]
        j = i-1
        while j >=0 and key < dizi[j] :
                dizi[j+1] = dizi[j]
                j -= 1
        dizi[j+1] = key
dizi = [12, 11, 13, 5, 6]
arayaEkleme(dizi)
print dizi
