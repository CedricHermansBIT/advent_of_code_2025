from functools import reduce

# Part 1
lines=[]
with open("input.txt") as ifile:
    for line in ifile:
        lines.append([x for x in line.strip().split(" ") if x != ""])

r=0
for x in zip(*lines):
    if x[-1] == "+":
        r+=reduce(lambda x,y:int(x)+int(y) , x[:-1])
    else:
        r+=reduce(lambda x,y:int(x)*int(y) , x[:-1])
print(r)

# Part 2
lines_no_spaces=[]
with open("input.txt") as ifile:
    for line in ifile:
        lines_no_spaces.append([x for x in line.strip().split(" ") if x!= ""])
print(lines_no_spaces)
max_numbers_per_col=[]
for x in zip(*lines_no_spaces):
    max_numbers_per_col.append(max([len(y) for y in x]))

print(max_numbers_per_col)
lines_wi_spaces=[]
with open("input.txt") as ifile:
    for line in ifile:
        lines_wi_spaces.append([])
        start=0
        for i in max_numbers_per_col:
            lines_wi_spaces[-1].append(line[start:start+i])
            start+=i+1
print(lines_wi_spaces)

r=0
for x in zip(max_numbers_per_col, *lines_wi_spaces):
    m=x[0]
    x=x[1:]
    numbers=[]
    for i in range(m):
        t=""
        for n in x[:-1]:
            t+=n[i]
        numbers.append(int(t))
    if "+" in x[-1]:
        r+=reduce(lambda x,y:x+y , numbers)
    else:
        r+=reduce(lambda x,y:x*y , numbers)
print(r)
