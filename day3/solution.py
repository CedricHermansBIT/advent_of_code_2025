import time

st=time.time()
#Part 1
r=0
with open("input.txt") as ifile:
    for line in ifile:
        y=list(line.strip())
        s=set()
        for n,i in enumerate(y[:-1]):
            for m,j in enumerate(y[n+1:]):
                s.add(int(i+j))
        r+=max(s)

print(r)
print(time.time()-st)

#Part 2
st=time.time()
def find_max(s):
    s=list(s)
    return max(s),s.index(max(s))

r=0
with open("input.txt") as ifile:
    for line in ifile:
        first=0
        highest=""
        for k in range(11,-1,-1):
            if k==0:
                s=line.strip()[first:]
            else:
                s=line.strip()[first:-k]
#            print(k,s)
            x,f=find_max(s)
            first+=f+1
            highest+=x
        r+=int(highest)
#        print(highest)
print(r)
print(time.time()-st)


#Redo part 1 in part2 style (faster):
st=time.time()
def find_max(s):
    s=list(s)
    return max(s),s.index(max(s))

r=0
with open("input.txt") as ifile:
    for line in ifile:
        first=0
        highest=""
        for k in range(1,-1,-1):
            if k==0:
                s=line.strip()[first:]
            else:
                s=line.strip()[first:-k]
#            print(k,s)
            x,f=find_max(s)
            first+=f+1
            highest+=x
        r+=int(highest)
#        print(highest)
print(r)
print(time.time()-st)
