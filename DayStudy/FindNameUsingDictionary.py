'''
Find name using dictionary.
input : list has there are n names.
output : Repeated name group in there are n name group.
'''

def find_same_name(a):
  name_dict={}    #step1. Make a dictionary each name counted number
  for name in a:    #Repeat to search for list "a".
    if name in name_dict:    #Same name find in list "a".
      name_dict[name] += 1    #Find same name and count 1.
    else:    # or not
      name_dict[name]=1    #Just 1.
  #step2. 2 over names, insert to New dictionary
  result=set()    #Save to result.
  for name in name_dict:    #name_dict data Sequential iteration
    if name_dict[name]>=2:
      result.add(name)

  return result

name=["Tom", "Jerry", "Mike", "Tom"]    #Warnning capital letter and minuscule
print(find_same_name(name))

name2=["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))
