# 리스트의 모든 원소를 스캔하기(enumerate() 함수 사용 - 1부터 카운트)

x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x, 1):
    print(f'{i}번째 = {name}')
