graph={
    'v': [['a',5],['b',8]],
    'a': [ ['b',2] , ['c',12]],
    'b': [ ['d',6], ['e',10]],
    'c': [['f',5]],
    'd':[ [ 'f',12], ['c',3] , ['e',2]],
    'e': [ ['f',7]]
}
# print("number of vertex")
# n = int(input())

# print("Mention all the vertcies")
# for i in range(n):
#     s=input()
#     graph[s]=[]
# print("Number of Edges")
# n=int(input())
# print("Now add edges with weights and give input as A B x(then press enter each entry of A or B or x)")
# for i in range(n):
#     ed1=input()
#     ed2=input()
#     ed3=input()
#     graph[ed1].append([ed2,int(ed3)])

print("give start and goal vertex")
start=input()
goal=input()

p_q=[]
# print(graph)
def next(s):
    p=graph[s[1][-1]]
    q=[]
    for i in range(len(p)):
            p_q.append([s[0]+p[i][1],s[1]+p[i][0]])

    p_q.sort()


def ucs(s):
    p_q.append([0,s])
    while p_q:
        st=p_q[0]
       
        if p_q[0][1][-1]==goal:
            print(p_q[0])
            return
            
        next(p_q[0])
        p_q.pop(0)

ucs(start)