def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list} # id_list에 입력되는 id들을 dict의 x로 받음

    for r in set(report): # report를 set 형식의 r로 반환
        reports[r.split()[1]] += 1 # 신고받은 id에 해당하는 value 값에 1씩 더함

    for r in set(report): # report를 set 형식의 r로 반환
        if reports[r.split()[1]] >= k: # 신고받은 id에 해당하는 value 값이 k보다 크다면
            answer[id_list.index(r.split()[0])] += 1 # 신고한 id의 index 값 : answer 안에서 0
                                                    # 신고한 id의 answer value에 1씩 더함

    return answer