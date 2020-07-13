from collections import deque
# BFS : Queue를 이용하여 탐색 (deque : 양방향 큐)
# 너비우선탐색(BFS)
# 그래프 : 해쉬테이블을 이용

# graph = dict()
graph = {}

graph["you"] = ["alice", "bob", "clare"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["clare"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []



# 판매원인지 알아내는 함수
def person_is_seller(name):
    return name[-1] == 'm'                  # m으로 끝나는지 확인

def search(name):
    search_queue = deque()                  # 새 큐를 생성
    search_queue += graph[name]             # 모든 이웃을 큐에 추가
    searched = []                           # 이미 확인한 사람을 추적하기 위한 배열
    while search_queue:                     # 큐가 비어있지 않으면 반복
        person = search_queue.popleft()     # 큐에서 첫번째 사람을 꺼낸다.
        if not person in searched:          # 이미 검색한 사람이 아니라면 확인
            if person_is_seller(person):    # 판매원인지 확인
                print(person + " is a MANGO seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False

search("you")