'''
FindFakeCoin2
input : All coins position, start and end point. (0,n-1)
output : Fake coin position number.
'''

'''
Measure weight Method.
a to b coins, c to d coins compare weight.
If a to b has fake coins(weight light) : display "-1"
If c to d has fake coins(weight light) : display "1" 
They are not have fake coin(same weight) : display "0"
'''

def weigh(a,b,c,d):
    fake=29    #Positions for fake coin(Algorithm must be used weight method, about find this position.)
    if a <= fake and fake <=b:
        return -1
    if c <= fake and fake <=d:
        return 1
    return 0
def find_fakecoin(left, right):
    if left == right:    #End condition. Find just one fake coin in range.
        return left
    half=(right-left+1)//2    #Divide two group that range is left to right.
    g1_left=left    #Group 1
    g1_right=left+half-1
    g2_left=left+half    #Group 2
    g2_right=g2_left+half-1
    result = weigh(g1_left, g1_right, g2_left, g2_right)    #Use weigh method
    if result==-1:    #If group 1 weight light. 
        return find_fakecoin(g1_left, g1_right)
    elif result ==1:    #If group 2 weight light.
        return find_fakecoin(g2_left,g2_right)
    else:    #If same weight two group.
        return right    #Then last one coin is fake.


n=100
print(find_fakecoin(0,n-1))