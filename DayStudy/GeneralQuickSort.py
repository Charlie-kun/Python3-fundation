'''
Input : list "a"
Output : nothing
In list "a" select of sort start and end range.
'''

def quick_sort_sub(a,start, end):
    if end-start<=0:    #quit condition
        return
    pivot=a[end]    #select standard component
    i=start
    for j in range(start, end):
        if a[j]<=pivot:
            a[i], a[j]=a[j], a[i]
            i+=1
    a[i], a[end]=a[end], a[i]
    quick_sort_sub(a,start,i-1)    #Component value group smaller than Standard component value
    quick_sort_sub(a,i+1, end)    #Component value group bigger than Standard component value

def quick_sort(a):
    quick_sort_sub(a,0,len(a)-1)

d=[6,8,3,9,10,1,2,4,7,5]
quick_sort(d)
print(d)