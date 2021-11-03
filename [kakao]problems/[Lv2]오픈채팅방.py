#https://programmers.co.kr/learn/courses/30/lessons/42888

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
def solution(record):
    id_dic = {}
    answer = []
    for sen in record:
        sen = sen.split(' ')

        print(sen)
        if sen[0]=='Enter':
            id_dic[sen[1]]=sen[2]
            answer.append([sen[1],'님이 들어왔습니다.'])
        if sen[0] == 'Leave':
            answer.append([sen[1],'님이 나갔습니다.'])
        if sen[0] == 'Change':
            id_dic[sen[1]] = sen[2]

    for i, log in enumerate(answer):
        log[0]=id_dic[log[0]]
        answer[i]=log[0]+log[1]

    return answer


print(solution(record))
# >>>['Prodo님이 들어왔습니다.', 'Ryan님이 들어왔습니다.', 'Prodo님이 나갔습니다.', 'Prodo님이 들어왔습니다.']