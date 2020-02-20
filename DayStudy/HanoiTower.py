'''
Hanoi Tower
Input : disk Number "n"
        first post "from_pos"
        finish post "to_pos"
        second post "aux_pos"
Output : disk move step
'''

def hanoi(n, from_pos, to_pos, aux_pos):
    if n==1:    #If just one disk move problem. Just carry one disk.
        print(from_pos, "->", to_pos)
        return

# move disk "n-1" Number move form to_pos
#hanoi(n-1, from_pos, aux_pos, to_pos)

#Most big disk "n-1" number carry to finish post
#print(from_pos, "->", to_pos)

#Disk number "n-1" in aux_pos move to finish_post.
#hanoi(n-1, aux_pos, to_pos, from_pos)

print("n=1")
hanoi(1,1,3,2)
#Number 1 disk move to post 1 to 3.

print("n=2")
hanoi(2,1,3,2)
#Number 2 disk move to post 1 to 3.

print("n=3")
hanoi(3,1,3,2)
#Number 3 disk move ro post 1 to 3.