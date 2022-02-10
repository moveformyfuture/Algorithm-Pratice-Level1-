def solution(lottos, win_nums):
    # lottos : 내가 선택한 로또 번호, win_nums : 당첨번호
    rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1} #Rank함수 이용해 주어진 순위 정보를 기입
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]
    #set=순서X, 중복X인 집합
    #lotto와 win_nums의 번호를 대조해 맞는 번호만 활용해 rank 계산
    #conut함수와 0의 정의를 활용해 최저 등수 계산 (0의 정의 : 알아볼 수 없는 번호)