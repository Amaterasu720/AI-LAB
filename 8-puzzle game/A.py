target=(
    (1,2,3),
    (4,5,6),
    (7,8,9)
)
pos={
    1 : [0,0],
    2 : [0,1],
    3 : [0,2],
    4 : [1,0],
    5 : [1,1],
    6 : [1,2],
    7 : [2,0],
    8 : [2,1],
    9 :[2,2]
}
ex=[[1,6,2]
    ,[4,9,3],
    [7,5,8]]


    
start = tuple(tuple(i) for i in ex )

print("Give type of heuristic used") 
h_type=int(input())       

p_q=[]
vis={}
g={}
h={}
path={}

def heur(type,a):
    h[a]=0
    if type==1:
        h[a]=0

    elif type ==2:
        dis=0
        for i in range(3):
            for j in range(3):
                k = a[i][j]
                if pos[k] != [i,j] and k!=9:
                    dis+=1
        h[a]=dis

    elif type==3:
        dis=0
        for i in range(3):
            for j in range(3):
                k = a[i][j]
                if k !=9:
                    dis+= abs(pos[k][0]-i) + abs(pos[k][1]-j)
        h[a]=dis

    elif type ==4:
       dis=0
       for i in range(3):
            for j in range(3):
                k = a[i][j]
                if pos[k] != [i,j]:
                   dis+= 9 - (abs(pos[k][0]-i)+1)*(abs(pos[k][1]-j)+1)

       h[a]=dis
            
    
def next(a1,type):
        x=-1
        y=-1
        for i in range(3):
            for j in range (3):
                if a1[i][j]==9:
                    x=i
                    y=j
                    break
            if x !=-1:
                break
        cost=g[a1]
        a=list(list(i) for i in a1)
        
        if x>0:
            a[x][y],a[x-1][y]=a[x-1][y],a[x][y]
            a1=tuple(tuple(i) for i in a )
            if a1 not in vis:
                g[a1]=cost+1
                heur(type,a1)
                j=g[a1] + h[a1]
                # print(type(j))
                vis[a1]=1
                p_q.append([j,a1])

            a=list(list(i) for i in a1)
            a[x][y],a[x-1][y]=a[x-1][y],a[x][y]


        if y>0:
            a[x][y],a[x][y-1]=a[x][y-1],a[x][y]
            a1=tuple(tuple(i) for i in a )
            if a1 not in vis:
               g[a1]=cost+1
               heur(type,a1)
               j=g[a1] + h[a1]
            #  print(type(j))
               vis[a1]=1
               p_q.append([j,a1]) 

            a=list(list(i) for i in a1)
            a[x][y],a[x][y-1]=a[x][y-1],a[x][y]


        if x<2:
            a[x][y],a[x+1][y]=a[x+1][y],a[x][y]
            a1=tuple(tuple(i) for i in a )
            if a1 not in vis:
                g[a1]=cost+1
                heur(type,a1)
                j=g[a1] + h[a1]
                # print(type(j))
                vis[a1]=1
                p_q.append([j,a1])

            a=list(list(i) for i in a1)
            a[x][y],a[x+1][y]=a[x+1][y],a[x][y]


        if y<2:
            a[x][y],a[x][y+1]=a[x][y+1],a[x][y]
            a1=tuple(tuple(i) for i in a )
            if a1 not in vis:
                g[a1]=cost+1
                heur(type,a1)
                j=g[a1] + h[a1]
                # print(type(j))
                vis[a1]=1
                p_q.append([j,a1])
                

            a=list(list(i) for i in a1)
            a[x][y],a[x][y+1]=a[x][y+1],a[x][y]
        
        if type!=1 :
            p_q.sort()


def A_star(a,h_type):
        
        g[a]=0
        heur(h_type,a)
        p_q.append([g[a]+h[a],a])
        vis[a]=1
        while p_q:
            s=len(p_q)
            v=p_q[0][1]
            print(p_q[0])

            path[g[v]]=v
            p_q.pop(0)
            if v== target:
               
                print("done")
                print("length of path used" , g[v])
                break
            next(v,h_type)

def monotonecheck():
   for i in range(len(path)):
        print(path[i])

        



   
# print("h type 2")
# A_star(start,2)
# print("states used ",len(vis))
# monotonecheck()
# p_q.clear()
# vis.clear()
# g.clear()
# h.clear()

print("h type 3")
A_star(start,3)
print("states used ",len(vis))
monotonecheck()
p_q.clear()
vis.clear()
g.clear()
h.clear()

print("h type 1")
A_star(start,1)
print("states used ",len(vis))
p_q.clear()
vis.clear()
g.clear()
h.clear()


# print("h type 4")
# A_star(start,4)
# print("states used ",len(vis))
# p_q.clear()
# vis.clear()
# g.clear()
# h.clear()
