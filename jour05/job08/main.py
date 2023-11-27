def my_sort(t): 
    n = len(t)
    a = 0 
    for i in range(0,n-1):
        min = i
        for j in range(i+1,n):
            if t[j] < t[min]:
                min = j 
            if min != i :
                t[i] , t[min] = t[min], t[i] 
    a = i + j
    print("Liste trié :",t,"Nombre de coup total :",a)

my_sort([7, 11, 42, 39, 2])
my_sort([7, 11, 42, 39, 2,15,40,32,85,4,1])