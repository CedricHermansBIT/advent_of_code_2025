with open("input.txt") as ifile:
    lines=[line.strip() for line in ifile]

# Part 1
tachyons=set()
tachyons.add(lines[0].index("S"))

r=0
for line in lines[1:]:
    new_tachyons=set()
    for tachyon in tachyons:
        if line[tachyon]!="^":
            new_tachyons.add(tachyon)
        else:
            r+=1
            new_tachyons.add(tachyon-1)
            new_tachyons.add(tachyon+1)
    tachyons=new_tachyons
print("Final tachyons =",len(tachyons))
print("   Times split =", r)

# Part 2
x=lines[0].index("S")

from functools import lru_cache

@lru_cache()
def recursive_traverse(x,y=1):
#    print(x,y)
    if y==len(lines)-1:
        return 1
    if lines[y][x]!="^":
        return recursive_traverse(x,y+1)
    else:
        a=recursive_traverse(x-1,y+1)
        b=recursive_traverse(x+1,y+1)
        return a+b

print("Final quantum tachyons =", recursive_traverse(x))
