from time import time
# Part 1
r=0
x=50
with open("input.txt") as ifile:
    for line in ifile:
        d=line[0]
        n=int(line[1:])
        match d:
            case "L":
                x-=n
            case "R":
                x+=n
        x%=100
        if x==0:
            r+=1
print("p1: ",r)

# Part 2
s=time()
r=0
x=50
with open("input.txt") as ifile:
    prev_null=False
    for line in ifile:
        d=line[0]
        n=int(line[1:])
        r+=n//100
        n%=100
        match d:
            case "L":
                x-=n
                if x<0 and not prev_null:
                    r+=1
            case "R":
                x+=n
                if x>100:
                    r+=1
        x%=100
        if x==0:
            r+=1
            prev_null=True
        else:
            prev_null=False
print("p2: ",r)
print(time()-s)