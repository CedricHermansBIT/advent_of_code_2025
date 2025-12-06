# Part 1

ranges=[]
in_numbers=False
r=0
with open("input.txt") as ifile:
    for line in ifile:
        if line.strip()=="":
            in_numbers=True
            continue
        if in_numbers:
            found=False
            n=int(line.strip())
            for k,v in ranges:
                if n>=k and n<=v:
                    r+=1
                    found=True
                    break
            if found:
                continue
        else:
            s,e = map(int,line.strip().split("-"))
            ranges.append((s,e))
print(ranges)
print(r)

# Part 2
ranges=[]
with open("input.txt") as ifile:
    for line in ifile:
        if line.strip()=="":
           break
        else:
            s,e = map(int,line.strip().split("-"))
            ranges.append((s,e))
ranges.sort(key=lambda x: x[0])

new_ranges=[]
i=0
# Not using a for loop, because it doesn't play nicely when popping items
while i < (len(ranges)-1):
    s1,e1 = ranges[i]
    # Too lazy to adapt this to also a while loop, so keep track with counter how many we pop
    # Then adjust index so it doesn't go out of the list
    l=0
    for j in range(i+1,len(ranges)):
        s2,e2 = ranges[j-l]
        # Since list is sorted, s1 is always <= s2, we just need to check of new end is > than old
        if s2<=e1:
            if e2>e1:
                # if so, replace old end by new
                e1=e2
            # Remove that range from list, because otherwise it would create duplicates
            ranges.pop(j-l)
            l+=1
        else:
            # if new start is bigger than the end, since list is sorted, no need to check following numbers, continue with next range instead
            break
    # but before continuing, ofcourse save the biggest range to a new list
    new_ranges.append((s1,e1))
    i+=1

print(new_ranges)
r=0
# count the width of each
for k,v in new_ranges:
    r+=v-k+1
# shorter way ;p
print(sum([v-k+1 for (k,v) in new_ranges]))
print(r)
