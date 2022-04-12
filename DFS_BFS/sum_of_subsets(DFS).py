# 백준 1182
import sys
inp = sys.stdin.readline
n, s = map(int, inp().split())
print(n,s)
arr = list(map(int, inp().split()))

cnt=0 # 부분합이 s랑 같게 될 경우의 수
def subset_sum(idx, sub_sum): # sub_sum도 0에서 시작
    global cnt
    if idx>=n:
        return # loop에서의 break와 같은 역할
    sub_sum += arr[idx] # array에 있는 원소 더함

    if sub_sum==s:
        cnt+=1
    
    subset_sum(idx+1, sub_sum)

    subset_sum(idx+1, sub_sum - arr[idx])

subset_sum(0, 0) 
print(cnt)    
