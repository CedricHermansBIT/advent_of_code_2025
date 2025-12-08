# Part1
boxes=[]
with open("input.txt") as ifile:
    for line in ifile:
        boxes.append(tuple([x for x in map(int,line.strip().split(","))]))

#print(boxes)
def dist(a,b):
    (x1,y1,z1)=a
    (x2,y2,z2)=b
    return (x1-x2)**2+(y1-y2)**2+(z1-z2)**2

distances_boxes={}
for i in range(len(boxes)-1):
    for j in range(i+1,len(boxes)):
        distances_boxes[dist(boxes[i],boxes[j])]=(boxes[i],boxes[j])

distances=list(distances_boxes.keys())
distances.sort()
#print(distances_boxes)
#print(distances)

groups=[]
for distance in distances[:1001]:
    a,b = distances_boxes[distance]
    found=False
    foundgroup=set()
    for group in groups:
        if a in group or b in group:
            group.add(a)
            group.add(b)
            # We do this check to see if we have like 2 groups, where one group contains a, and another group b, because now we need to combine them in one big group
            if found:
                group_copy=group.copy()
                groups.remove(group)
                groups.remove(foundgroup)
                foundgroup=foundgroup.union(group_copy)
                groups.append(foundgroup)
                # Normally no other groups can contain either a or b, each can only be in one group, so no need to actually check the rest now
                break
            foundgroup=group.copy()
            found=True
    if not found:
        group=set()
        group.add(a)
        group.add(b)
        groups.append(group)

#print(groups)
lengths=[len(group) for group in groups]
lengths.sort(reverse=True)

#print(lengths)

r=1
for x in lengths[0:3]:
    r*=x
print(r)

# Part2
groups=[]
i=0
while i==0 or len(boxes)!=len(groups[0]):
    a,b = distances_boxes[distances[i]]
    found=False
    foundgroup=set()
    for group in groups:
        if a in group or b in group:
            group.add(a)
            group.add(b)
            if found:
                group_copy=group.copy()
                groups.remove(group)
                groups.remove(foundgroup)
                foundgroup=foundgroup.union(group_copy)
                groups.append(foundgroup)
                break
            foundgroup=group.copy()
            found=True
    if not found:
        group=set()
        group.add(a)
        group.add(b)
        groups.append(group)
#    print(max([len(group) for group in groups]))
    i+=1
print(a[0]*b[0])
