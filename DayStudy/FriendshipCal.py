'''
Calculate friendship in friends list
input : friend graph "g", start point "me"
output : every friends name and friendship parameter
'''

def print_all_friends(g, start):
  qu=[]    #memorize point 1. Save at friends name, friendship
  done=set()    #memorize point 2. already inserted friends in qu.and
  qu.append((start,0))    #(friend name, friendship) information tied one tuple.
  done.add(start)    #check for same name

  while qu:
    (p,d)=qu.pop(0)    #output at friend name, friendship information.
    print(p,d)    #display friend name, friendship
    for x in g[p]:    #Search for all list member
      if x not in done:    #Not inserted all list member in "done".
        qu.append((x,d+1))    #Insert friends name and friendship +1 at "qu"
        done.add(x)    #name saved.

fr_info={    #friend list
  'Summer':['John', 'Justin', 'Mike'],
  'John':['Summer', 'Justin'],
  'Justin':['John', 'Summer', 'Mike', 'May'],
  'Mike':['Summer', 'Justin'],
  'May':['Justin', 'Kim'],
  'Kim':['May'],
  'Tom':['Jerry'],
  'Jerry':['Tom']
}

print_all_friends(fr_info,'Summer')
print()
print_all_friends(fr_info,'Jerry')
