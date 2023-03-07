import random
n=int(input())
print(type(n))
s1=[[0]*n for i in range(n)]
for i in range(n):
    s1[0][i]=1

s=tuple(tuple(i) for i in s1 )
op=[]


vis={}
def ran(n,s):
    lis=[]
    for i in range(n):
        lis.append(i)

    random.shuffle(lis)
    s1=list(list(i) for i in s)
    s1=[[0]*n for i in range(n)]

    for i in range(n):
        s1[lis[i]][i]=1
    s=tuple(tuple(i) for i in s1 )
    return s

def heur(n,s):
    p=0
    for i in range(n):
        for j in range(n):
            if s[i][j]==1:
                x=i
                y=j
            
                while y<n-1:
                    y=y+1
                    if s[x][y]==1:
                        p=p+1
                        

                x=i
                y=j    
                while x<n-1 and y<n-1:
                    x=x+1
                    y=y+1
                    if s[x][y]==1:
                        p=p+1
                x=i
                y=j
                while y<n-1 and x>0:
                    x=x-1
                    y=y+1
                    if s[x][y]==1:
                        p=p+1

    return p

def next(n,s,cost):
    s1=list(list(i) for i in s)
    for i in range(n):
        for j in range(n):
            if s1[i][j]==1:
                # print(i,j)
                if i!=n-1:
                    s1[i][j],s1[i+1][j]=s1[i+1][j],s1[i][j]
                    s=tuple(tuple(i) for i in s1 )
                    if cost>heur(n,s) and s not in vis:
                        op.append(s)
                        vis[s]=1
                        return s
                    s1=list(list(i) for i in s)
                    s1[i][j],s1[i+1][j]=s1[i+1][j],s1[i][j]
                else:
                    s1[i][j],s1[0][j]=s1[0][j],s1[i][j]
                    # print(s1)
                    s=tuple(tuple(i) for i in s1 )
                    if cost>heur(n,s) and s not in vis:
                        op.append(s)
                        vis[s]=1
                        return s
                    s1=list(list(i) for i in s)
                    s1[i][j],s1[0][j]=s1[0][j],s1[i][j]
    while True:
        s=ran(n,s)
        if s not in vis:
            vis[s]=1
            return s

def hill(n,s):
    vis[s]=1
    t=0
    while True:
        s=next(n,s,heur(n,s))
        vis[s]=1
        if heur(n,s)==0:
            print(s)
            t=t+1
            print(len(vis))
        
        if t==3:
            break
          

hill(n,s)
print(len(vis))
print(len(op))