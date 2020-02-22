'''
SmallSort
input : list "a"
output : sort new list
'''
'''
def find_min_idx(a):
    n=len(a)
    min_idx=0;
    for i in range(1,n):
        if a[i]<a[min_idx]:
            min_idx=i
    return min_idx

def sel_sort(a):
    result=[]    #Make a new list and sort to new saved value.
    while a:    #Repeat for remained value.
        min_idx=find_min_idx(a)    #Most smallest values location. in list
        value=a.pop(min_idx)    #Finded most smallest values save to "value".
        result.append(value)
    return result

d=[2,4,5,1,3]
print(sel_sort(d))
'''

'''
select sort
input : list a
output : none
'''

def sel_sort(a):
    n=len(a)
    for i in range(0,n-1):    #repeat 0 to n-2
        min_idx=i    #Search at i th position to last end and find smallest value.
        for j in range(i+1, n):
           if a[j] < a[min_idx]:
               min_idx=j
        a[i], a[min_idx]=a[min_idx], a[i]    # Smallest value move to "value" position.

d=[2,4,5,1,3]
sel_sort(d)
print(d)