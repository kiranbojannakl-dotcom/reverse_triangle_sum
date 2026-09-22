# reverse triangle list problem
"""
input = 1,2,3,4,5
output=
[1, 2, 3, 4, 5]
[3, 5, 7, 9]
[8, 12, 16]
[20, 28]
[48]
"""

def compute_sum(s):
    sum_list=[]
    for i in range(len(s)-1):
        sum_=s[i]+s[i+1]
        sum_list.append(sum_)
    return sum_list
def triangle(res):
    while len(res)>1:
        sum_list=compute_sum(res)
        print(sum_list)
        res=sum_list
   
s=list(map(int,input().split(",")))
print(s)
triangle(s)