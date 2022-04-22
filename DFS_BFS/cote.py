# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

physics = list(map(int,input().split()))
history = list(map(int,input().split()))

N = len(physics)
p_avg=sum(physics)/N
h_avg=sum(history)/N
p_var, h_var,cov = 0,0,0
for i in range(N):
    p_var += (physics[i]-p_avg)**2
    h_var += (history[i]-h_avg)**2
    cov +=(physics[i]-p_avg)*(history[i]-h_avg)
# p_var, h_var, cov = p_var/(N-1),h_var/(N-1),cov/(N-1)
corr = cov/math.sqrt(p_var*h_var)
print(round(corr,3))

