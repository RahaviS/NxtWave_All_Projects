#Given two integers M and N, write a program to print rectangular
#pattern of M rows and N columns using symbol asterisk(*).

M=int(input())
N=int(input())
count=0
while count<M:
    print("* "*N)
    count=count+1 
    
