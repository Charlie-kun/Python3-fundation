'''
InsertSort
input : list "a"
output : sort new list
'''

#"r" list insert "v" and let knows "v" position

def find_ins_idx(r,v):
    #Already sort "r" list. first to end r component check for matching.
    for i in range(0,len(r)):
        if v<r[i]:   #if r[i] bigger than v
            return i    #return i.
    return len(r)    # but r[i] is not bigger than v. so, v insert last component

def ins_sort(a):
    result=[]    #Make a new array, sort components and save
    while a:    #repeat stop when list end read
        value=a.pop(0)    #pick up one from list
        ins_idx=find_ins_idx(result, value)    #find pick ons's location
        result.insert(ins_idx, value)    #insert to result
    return result

d=[2,4,5,1,3]
print(ins_sort(d))