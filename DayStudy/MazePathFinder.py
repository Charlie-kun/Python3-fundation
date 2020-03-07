'''
Maze Path Finder
Maze describe, named each alphabet sections.
input : Maze information "g", start point, end point
output : Solved maze path root is displayed string.
'''

def solve_maze(g, start, end):
  qu=[]    #memorize point 1. Path root saved
  done=set()    #memorize point 2. Checking for repeat alphabet section.

  qu.append(start)    #started point insert to "qu"
  done.add(start)    #inserted group too.

  while qu:     #If remained processing path.
    p=qu.pop(0)    #Getting up processing target.
    v=p[-1]    #Last alphabet at saved "qu" is processed now.
    if v==end:    #Last alphabet is end point
      return p    #Return find path until now
    for x in g[v]:    
      if x not in done:    #When not insert alphabet to "qu" yet.
        qu.append(p+x)    #Path insert at new alphabet.
        done.add(x)     #Insert group too.
  return "?"    #Nobody reached end point. Then return to "?".

#maze information
maze={
  'a':['e'],
  'b':['c', 'f'],
  'c':['b', 'd'],
  'd':['c'],
  'e':['a', 'i'],
  'f':['b','g','j'],
  'g':['f', 'h'],
  'h':['g', 'l'],
  'i':['e', 'm'],
  'j':['f','k', 'n'],
  'k':['j', 'o'],
  'l':['h', 'p'],
  'j':['f', 'k', 'n'],
  'k':['j', 'o'],
  'l':['h', 'p'],
  'm':['i', 'n'],
  'n':['m', 'j'],
  'o':['k'],
  'p':['l']
}

print(solve_maze(maze, 'a', 'p'))
