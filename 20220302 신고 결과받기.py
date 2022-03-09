# 문제 단순화
# 1. 신고는 1번만 인정(중복 인정X) --> set 사용
# 2. 신고된 유저 Count --> dict 사용
# 3. 신고 회수 k이상 : 제제 메일 발송

def solution(id_list, report, k):
    answer = [0] * len(id_list)  # result가 list형식, id_list의 n개의 원소 갯수 고려해서 answer 셋팅
    reports = {x: 0 for x in id_list}  # 기존 id_list 값에 x 값을 삽입 --> dic로 변환해서 신고횟수 count

    for r in set(report):  # report에서는 중복을 인정하지 않기 위해 set으로 자료형 변환
        reports[r.split()[1]] += 1  # reports(dict)에서 신고된 값에 1을 더함

    for r in set(report):
        if reports[r.split()[1]] >= k:  # 신고받은 유저에 해당하는 value 값이 k보다 크다면
            answer[id_list.index(r.split()[0])] += 1  # id_list에서 신고한 유저의 index를 추출
                                                      # index에 해당하는 answer값에 1씩 증가(id_list 순서 반영)

    return answer