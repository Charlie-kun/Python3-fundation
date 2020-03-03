'''
Find All Friends
input : friends relatioship graph, Searching start point "me"
output : All friends name.
'''

def print_all_friends(g, start):
  qu=[]    #Save point1. save queue
  done=set()    #Save point2. inserted friends in queue already.
  qu.append(start)    #"me" insert at queue.
  done.add(start)    #"me" insert at point2.

  while qu:    #queue has a processing.
    p=qu.pop(0)    #queue process target pick up.
    print(p)    #print name
    for x in g[p]:    #His friend... 
      if x not in done:    #insert to queue net yet.
        qu.append(x)    # insert queue
        done.add(x)    #insert point2.

'''
fiends relation ship map
A's friend list has 'B' so, B's friend list display 'A'.
'''
fr_infor={
  'Summer' : ['John', 'Justin', 'Mike'],
  'John' : ['Summer', 'Justin'],
  'Justin' : ['John', 'Summer', 'Mike', 'May'],
  'Mike' : ['Summer', 'Justin'],
  'May' : ['Justin', 'Kim'],
  'Kim' : ['May'],
  'Tom' : ['Jerry'],
  'Jerry' : ['Tom']
}

print_all_friends(fr_infor, 'Summer')
print()
print_all_friends(fr_infor, 'Jerry')
