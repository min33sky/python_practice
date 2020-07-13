# 다익스트라 알고리즘

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# 가격표
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 부모
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 중복 추적
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:                                      # 모든 정점을 확인한다.
        cost = costs[node]
        if cost < lowest_cost and node not in processed:    # 아직 처리하지 않은 정점중에서 싼 가격이 있다면
            lowest_cost = cost                              # 새로운 최저 정점으로 설정하자
            lowest_cost_node = node
    return lowest_cost_node



node = find_lowest_cost_node(costs)         # 가격표에서 아직 처리하지 않은 가장 싼 정점을 찾는다.
while node is not None:                     # 모든 정점을 처리하면 반복문 종료
    cost = costs[node]
    neighbors = graph[node]                 # 이 노드의 이웃들을 가져온다.
    for n in neighbors.keys():              # 모든 이웃에 대해 반복한다.
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:             # 만약 이 정점을 지나는 것이 가격이 더 싸다면
            costs[n] = new_cost             # 정점의 가격을 갱신하고
            parents[n] = node               # 부모를 이 정점으로 새로 설정
    processed.append(node)                  # 이미 처리한 정점으로 기록
    node = find_lowest_cost_node(costs)     # 반복

print(costs["fin"])
print(parents)
print(costs)
