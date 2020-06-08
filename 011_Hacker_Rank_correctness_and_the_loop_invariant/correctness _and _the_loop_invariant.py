# Wrong:
#def insertion_sort(l):
#    for i in range(1, len(l)):
#        j = i-1
#        key = l[i]
#        while (j > 0) and (l[j] > key):
#           l[j+1] = l[j]
#           j -= 1
#        l[j+1] = key

#Corrected:
def insertion_sort(ar):
    for i in range(1, len(ar)):
        j = i-1
        key = ar[i]
        while (j >= 0) and (ar[j] > key):
           ar[j+1] = ar[j]
           j -= 1
        ar[j+1] = key

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))