# Part 1
# Two oposite tiles
red_tiles=[]
with open("test.txt") as ifile:
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

tile_connections={}
for i in range(len(red_tiles)-1):
    tile1=red_tiles[i]
    tile_connections[tile1] = {"x":[], "y":[]}
    for j in range(len(red_tiles)):
        if i==j:
            continue
        tile2=red_tiles[j]
        if tile1[0]==tile2[0]:
            tile_connections[tile1]["x"].append(tile2)
        elif tile1[1]==tile2[1]:
            tile_connections[tile1]["y"].append(tile2)

print(tile_connections)
areas=[]
for tile, connections in tile_connections.items():
    print(tile,connections)
    dy=abs(tile[1]-connections["x"][0][1])+1
    dx=abs(tile[0]-connections["y"][0][0])+1
    areas.append(dx*dy)
print(max(areas))
