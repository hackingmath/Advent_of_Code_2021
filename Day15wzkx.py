#from wzkx on Reddit AoC thread
#https://www.reddit.com/user/wzkx/

d=[[int(c) for c in l.strip()] for l in open("C:\\Users\\Owner\\Documents\\AoC2021\\day15.txt","rt")]

def step(ij,v,p,u,w,N,I):
  # mark_from_ij
  v[ij]=True
  u.remove(ij)
  i,j=ij//N,ij%N
  for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
    if 0<=ni<N and 0<=nj<N:
      nij=N*ni+nj
      if v[nij]: continue
      if p[nij]>p[ij]+w[nij]:
        p[nij]=p[ij]+w[nij]
        u.append(nij)
  # min_unvisited
  mij=mp=I
  for uij in u:
    if p[uij]<mp:
      mij=uij; mp=p[uij]
  return mij

def solve(d):
  N=len(d); NN=N*N; I=999999 # infinity :)
  w=[] # weights, 1-dimension copy of input
  for i in range(N): w+=d[i]
  v=[False for j in range(NN)] # visited
  p=[I for j in range(NN)] # paths
  u=[] # unvisited items (ij indexes)
  p[0]=0 # start with top left corner
  u.append(0)
  uij = step(0,v,p,u,w,N,I)
  while uij!=I:
    uij = step(uij,v,p,u,w,N,I)
  return p[NN-1] # right bottom

def scale(a,K):
  N=len(a)
  g=[[0 for i in range(K*N)] for j in range(K*N)]
  for ii in range(K):
    for jj in range(K):
      for i in range(N):
        for j in range(N):
          g[ii*N+i][jj*N+j] = (a[i][j]-1+ii+jj)%9+1
  return g

print( solve(d) )
print( solve(scale(d,5)) ) #2893 Haven't submitted yet