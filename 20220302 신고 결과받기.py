def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list} # id_list에 입력되는 id들을 dict의 x로 받음

    for r in set(report):
        reports[r.split()[1]] += 1
        print(reports)

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer