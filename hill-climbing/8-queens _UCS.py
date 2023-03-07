n=int(input())
print(type(n))
s1=[[0]*n for i in range(n)]
for i in range(n):
    s1[0][i]=1

s=tuple(tuple(i) for i in s1 )

ans=[]
vis={}
p_q=[]
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
def next(n,s):
    s1=list(list(i) for i in s)
    # print(s1)
    for i in range(n):
        for j in range(n):
            if s1[i][j]==1:
                # print(i,j)
                if i!=n-1:
                    s1[i][j],s1[i+1][j]=s1[i+1][j],s1[i][j]
                    # print(s1)
                    s=tuple(tuple(i) for i in s1 )
                    if s not in vis:
                        p_q.append([heur(n,s),s])
                        vis[s]=1
                    s1=list(list(i) for i in s)
                    s1[i][j],s1[i+1][j]=s1[i+1][j],s1[i][j]
                else:
                    s1[i][j],s1[0][j]=s1[0][j],s1[i][j]
                    # print(s1)
                    s=tuple(tuple(i) for i in s1 )
                    if s not in vis:
                        p_q.append([heur(n,s),s])
                        vis[s]=1
                    s1=list(list(i) for i in s)
                    s1[i][j],s1[0][j]=s1[0][j],s1[i][j]

                
    p_q.sort()
    s=tuple(tuple(i) for i in s1 )

def hill(n,s):
    p_q.append([heur(n,s),s])
    vis[s]=1
    # print(len(p_q))
    while p_q:
       
        v=p_q[0][1]
        cost=p_q[0][0]
      
        if cost==0:
            print(v)
            print(len(vis))
            ans.append(v)
        p_q.pop(0)  
        next(n,v)
          

hill(n,s)
print(len(vis))
print(len(ans))
