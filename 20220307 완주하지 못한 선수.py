import collections # python이 제공하는 하나의 class

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion) # Counter : list를 가지고 Counter를 생성하면, Counter는 Key가 이름이고, Value가 count인 dic를 반환
    return list(answer.keys())[0] # 남아있는 key의 이름값을 반환