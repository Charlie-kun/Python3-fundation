#page 182. Find low price
#graph 
graph={}    # Drowing for hashtable
graph["start"]={}
graph["start"]["a"]=6
graph["start"]["b"]=2

graph["a"]={}
graph["a"]["fin"]=1

graph["b"]={}
graph["b"]["a"]=3
graph["b"]["fin"]=5

graph["fin"]={}

#가격 graph
infinity=float("inf")
costs={}
costs["a"]=6
costs["b"]=2
costs["fin"]=infinity

#부모 테이블
parents={}
parents["a"]="start"
parents["b"]="start"
parents["fin"]=None

processed=[]

def find_lowest_cost_node(costs):
    lowest_cost=float("inf")
    lowest_cost_node=None
    for node in costs:    #check all node
        cost=costs[node]    # Find cheap cost yet
        if cost<lowest_cost and node not in processed:
            lowest_cost=cost    #new cheaper cost
            lowest_cost_node=node
    return lowest_cost_node

node=find_lowest_cost_node(costs)    # Find a cheaper cost node
while node is not None:    #Every node find cost is done.
    cost=costs[node]
    neighbors=graph[node]
    for n in neighbors.keys():    #Every neighbors repeat
        new_cost=cost+neighbors[n]
        if costs[n]>new_cost:    #if costs node find New cheap cost
            costs[n]=new_cost    #Modified cost
            parents[n]=node    #Parents new selct
    processed.append(node)    #Record for node process
    node=find_lowest_cost_node(costs)    #And next node find

print("Cost form the start to each node:")
print(costs)
