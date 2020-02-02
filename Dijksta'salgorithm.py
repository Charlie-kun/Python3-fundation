#page 182. 가장 낮은 가격 찾기
#graph 그리기
graph={}    #그래프를 그리기 위한 해시테이블 생성
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
    for node in costs:    #모든 정점을 확인
        cost=costs[node]    # 아직 처리하지 않은 정점 중 더 싼것이 있으면
        if cost<lowest_cost and node not in processed:
            lowest_cost=cost    #새로운 최저 정점으로 설정
            lowest_cost_node=node
    return lowest_cost_node

node=find_lowest_cost_node(costs)    #아직 처리하지 않은 가장 싼 정점을 찾는다.
while node is not None:    #모든 정점을 처리하면 반복문이 종료
    cost=costs[node]
    neighbors=graph[node]
    for n in neighbors.keys():    #모든 이웃에 대해 반복
        new_cost=cost+neighbors[n]
        if costs[n]>new_cost:    #만약 이 정점을 지나는 것의 가격이 더 싸다면
            costs[n]=new_cost    #정점의 가격을 갱신
            parents[n]=node    #부모를 이 정점으로 새로 설정
    processed.append(node)    #정점을 처리한 사실을 기록
    node=find_lowest_cost_node(costs)    #다음 정점을 찾고 반복

print("Cost form the start to each node:")
print(costs)