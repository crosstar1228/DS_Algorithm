import sys

inp = sys.stdin.readline
n, s = map(int,inp().split())
sets = list(map(int, inp().split()))
ans=0
def backtrack(x,subset):# x는 sets에 대응될 index
    global ans
    if x>=n:
        return

    subset +=sets[x] #input으로 받은 부분합에 더함

    if subset==s:
        ans+=1
    # if subset<s: # 값들이 양수로만 이루어져 있을 경우 활용하면 좋을 조건
    backtrack(x+1, subset) # 해당 값을 더한 부분합.

    backtrack(x+1, subset-sets[x]) # 안더한 부분합.

backtrack(0,0)
print(ans)

