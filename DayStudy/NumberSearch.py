'''
Find select number in list(devid search)
input : list "a", find value "x"
output : Navigate "x" location. when navigate failed. display "-1"
'''

def binary_search(a,x):
    start=0
    end=len(a)-1

    while start<=end:    #When end of find "x". quit repeat.
        mid=(start+end)//2
        if x==a[mid]:
            return mid
        elif x>a[mid]:    #else if
            start=mid+1
        else:
            end=mid-1

    return -1

d=[1,4,9,16,25,36,49,64,81]
print(binary_search(d,36))    #5
print(binary_search(d,50))    #-1