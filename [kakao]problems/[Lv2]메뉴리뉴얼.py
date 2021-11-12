orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
ans=[]
from itertools import combinations
def solution(orders, course):
    for num in sorted(course,reverse=True):
        freq=[]
        cnt={}
        for i,comb in enumerate(orders):
            orders[i]=list(comb)
            freq+=list(combinations(orders[i],num))
        for key in freq:
            try:
                cnt[key]+=1
            except:
                cnt[key]=1
        # print(cnt)
        for tup in cnt.items():
            if tup[1]>1:

                ans.append(tup)
    # print(ans)
    for i,tup in enumerate(ans):
        for j,tupl in enumerate(ans):
            if tup!=tupl and type(tup)==tuple and type(tupl)==tuple :
                if set(''.join(tupl[0]))<set(''.join(tup[0])):
                    if tupl[1]<=tup[1]:
                        ans[j]=0
    answer=[]
    for tup in ans:
        if tup!=0:
            answer.append(''.join(tup[0]))
    return sorted(answer)
print(solution(orders,course))

        # for alpha in ans:
        #     if set(''.join(tup[0])) > set(''.join(alpha[0])) or alpha!=''.join(tup[0]):
        #         if tup[1]>alpha[1]:
        #             print('하이' + ''.join(tup[0]))
        #         continue



            # ans.append(''.join(tup[0]))
            # print(''.join(tup[0]))


    # set(tup[0]) > set(alpha) or
    # print(freq)

# print(set((['BCFG','CDF'])))
# print(set(('BG'))<set((['BCFG','CDF'])))