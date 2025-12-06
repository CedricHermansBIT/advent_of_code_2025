# Part 1
r=0
x=50
with open("input1.txt") as ifile:
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
r=0
x=50
with open("input1.txt") as ifile:
    for line in ifile:
        d=line[0]
        n=int(line[1:])
        match d:
            case "L":
                while n!=0:
                    n-=1
                    x-=1
                    x%=100
                    if x==0:
                        r+=1
            case "R":
                while n!=0:
                    n-=1
                    x+=1
                    x%=100
                    if x==0:
                        r+=1
print("p2: ",r)
