from time import sleep
import sys
# Problem 1

ENABLE_CONWAY=True

with open("input.txt") as ifile:
    text=ifile.readlines()

# Edges are border case, so we just add an "empty border"
# This makes it easier if we loop from 1 to n-1
# Then we don't need to check: if we are at 0, we can't go to the left
# Because now we can! Because we add an empty border to left and right
for n,i in enumerate(text):
    text[n]="."+i.strip()+"."

# Also add an empty border to top and bottom
length=len(text[0])
text.insert(0, "".join(["." for _ in range(length)]))
text.append("".join(["." for _ in range(length)]))

r=0
# loop over every position (but not the edges)
for y in range(1,len(text)-1):
    for x in range(1,length-1):
        # if it is a ".", we don't care about their neighbours
        if text[y][x] != "@":
            continue
        # Keep track of how many neighbours we have
        counter=0
        # Now we just need to check all surrounding cells, we can use offsets for this:
        # y-1 gets previous row, y+1 next, and then we can offset x to left and right.
        # Combination of these gets you all cells surrounding + including itself
        for y2 in [-1,0,1]:
            for x2 in [-1,0,1]:
                if ((y2==0) and (x2==0)):
                    # Don't count yourself, because we only want neighbours. Not self
                    continue
                # If we have an @ neighbour: add 1 to counter
                if text[y+y2][x+x2] == "@":
                    counter+=1
        # if this @ has <4 neighbours: this is 1 for our answer, so add it to result
        if counter<4:
            r+=1
print(r)


# Problem 2

def do_step(lines):
    lines_copy=lines.copy()
    r=0
    for y in range(1,len(lines)-1):
        for x in range(1,length-1):
            if lines[y][x] != "@":
                continue
            counter=0
            for y2 in [-1,0,1]:
                for x2 in [-1,0,1]:
                    if ((y2==0) and (x2==0)):
                        continue
                    if lines[y+y2][x+x2] == "@":
                        counter+=1
            if counter<4:
                spline=list(lines_copy[y])
                spline[x]="."
                lines_copy[y]="".join(spline)
#                print(f"line y goes from {lines[y]} to {lines_copy[y]}")
#                print(y,x)
                r+=1
    return r,lines_copy

res=0
r=-1
# Take a copy so we can use text in game of life ;p
text_copy=text.copy()
while r!=0:
    sys.stdout.write('\033[H')
    print("\n".join(text_copy))
    sleep(0.1)
    (r,text_copy)=do_step(text_copy)
#    print(r)
    res+=r
print(res)


# This is basically conways game of life, so let's just implement that as well

def do_conway(lines):
    lines_copy=lines.copy()
    for y in range(1,len(lines)-1):
        for x in range(1,length-1):
            # For game of life, we are interested in all positions, not only @
#            if lines[y][x] != "@":
#                continue
            counter=0
            for y2 in [-1,0,1]:
                for x2 in [-1,0,1]:
                    if ((y2==0) and (x2==0)):
                        continue
                    if lines[y+y2][x+x2] == "@":
                        counter+=1
            # Difference is that we just do a little bit different conditions and we can turn "." back into "@"
            if (counter>3) or (counter<2):
                # This could be done more efficiently if we would just store the grid as a list of lists so we don't need to split and join again
                # Even better would be to just store it as numbers. But since the size of grid is not that big, it is fast enough anyways.
                spline=list(lines_copy[y])
                spline[x]="."
                lines_copy[y]="".join(spline)
            elif counter==3:
                spline=list(lines_copy[y])
                spline[x]="@"
                lines_copy[y]="".join(spline)
#                print(f"line y goes from {lines[y]} to {lines_copy[y]}")
#                print(y,x)
    return lines_copy

if ENABLE_CONWAY:
    input("Press enter to start game of life")
    while True:
        sys.stdout.write('\033[H')
        print("\n".join(text))
        sleep(0.1)
        text=do_conway(text)
