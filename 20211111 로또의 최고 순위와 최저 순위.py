# 문제 단순화
# 최고 순위 : 맞춘 개수 + 모르는 개수
# 최저 순위 : 맞춘 개수

def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]  # 순위를 지정해야 하므로 rank(등수)를 list로 선언
    unknown = lottos.count(0)  # 알아볼 수 없는 수 0의 개수를
    ans = 0  # 맞춘 개수 초기화

    for x in win_nums:  # win_nums와 lottos를 대조
        if x in lottos:  # lottos 안에 x 가 있는지 조회
            ans += 1
    return rank[ans + unknown], rank[ans]