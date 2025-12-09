# Part 1
# Two oposite tiles
red_tiles=[]
with open("input.txt") as ifile:
    for line in ifile:
        red_tiles.append(tuple(int(x) for x in line.strip().split(",")))

print(red_tiles)
areas=[]
for i in range(len(red_tiles)-1):
    tile1=red_tiles[i]
    for j in range(i+1,len(red_tiles)):
        tile2=red_tiles[j]
        area=(abs(tile1[0]-tile2[0])+1) * (abs(tile1[1]-tile2[1])+1)
        areas.append(area)
print(max(areas))

# Part 2
# basically you just need 3 corners now instead of 2, or 2 in a straight line
# ach not so easy as first thought: the fourthe corner can be cut out...

# Extract x and y coords
x_coords=[x[0] for x in red_tiles]
y_coords=[x[1] for x in red_tiles]

# Make coords unique
x_coords=list(set(x_coords))
y_coords=list(set(y_coords))

# Sort them
x_coords.sort()
y_coords.sort()

# Compress regions by using indexes in x,y coords instead of real coords
compressed_regions=[]
for tile in red_tiles:
    x=x_coords.index(tile[0])
    y=y_coords.index(tile[1])
    compressed_regions.append((x,y))
print(compressed_regions)

tile_connections={}
for i in range(len(compressed_regions)-1):
    tile1=compressed_regions[i]
    tile_connections[tile1] = {"x":"", "y":""}
    for j in range(len(compressed_regions)):
        if i==j:
            continue
        tile2=compressed_regions[j]
        if tile1[0]==tile2[0]:
            tile_connections[tile1]["x"]=tile2
        elif tile1[1]==tile2[1]:
            tile_connections[tile1]["y"]=tile2

print(tile_connections)

field=[["." for j in range(len(x_coords))] for i in range(len(y_coords))]

for tile, connections in tile_connections.items():
    print(tile,connections)
    min_y = min(tile[1], connections["x"][1])
    max_y = max(tile[1], connections["x"][1])
    for y in range(min_y,max_y+1):
        field[y][tile[0]]="X"

    min_x= min(tile[0], connections["y"][0])
    max_x= max(tile[0], connections["y"][0])
    print(y,min_x,max_x)
    for x in range(min_x,max_x+1):
        field[tile[1]][x]="X"

# indicate corners
for tile in compressed_regions:
    field[tile[1]][tile[0]]="#"

# flash fill
# this is kinda a hack by looking at the field, should actually use a better method for more general solution
#for test
#to_check=[(field[1].index("#")+2,1)]
#for input
to_check=[(field[1].index("X")+1,1)]
checked=set()

while len(to_check):
    cell=to_check.pop()
    field[cell[1]][cell[0]]="X"
    checked.add(cell)
    neighbours=[(cell[0],cell[1]-1), (cell[0],cell[1]+1), (cell[0]-1, cell[1]), (cell[0]+1, cell[1])]
    for neighbour in neighbours:
        if neighbour not in checked:
            if field[neighbour[1]][neighbour[0]]==".":
                to_check.append(neighbour)
for row in field:
    print("".join(row))

def check_valid(x,y,dx,dy):
    for j in range(y,y+dy):
        for i in range(x,x+dx):
            if field[j][i] == ".":
                return False
    return True

areas={}
for i,tile1 in enumerate(compressed_regions[:-1]):
    for tile2 in compressed_regions[i+1:]:
        #print(tile,connections)
        dy=abs(tile1[1]-tile2[1])+1
        dx=abs(tile1[0]-tile2[0])+1
        if check_valid(min(tile1[0],tile2[0]),min(tile1[1],tile2[1]),dx,dy):
#            print("valid:",min(tile1[0],tile2[0]),min(tile1[1],tile2[1]),dx,dy)
            actual_dy=abs(y_coords[tile1[1]]-y_coords[tile2[1]])+1
            actual_dx=abs(x_coords[tile1[0]]-x_coords[tile2[0]])+1
            areas[actual_dy*actual_dx]=[tile1,tile2]

# because I want to know where the area is:
tile1,tile2=areas[max(areas)]
min_y = min(tile1[1], tile2[1])
max_y = max(tile1[1], tile2[1])
for y in range(min_y,max_y+1):
    min_x= min(tile1[0], tile2[0])
    max_x= max(tile1[0], tile2[0])
    for x in range(min_x,max_x+1):
        field[y][x]="@"

for row in field:
    print("".join(row))

print(max(areas))

