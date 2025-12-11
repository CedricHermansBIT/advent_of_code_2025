conn=dict()

with open("input.txt") as ifile:
    for line in ifile:
        key,val = line.strip().split(": ")
        vals=val.split(" ")
        conn[key]=vals
print(conn)

from functools import lru_cache

@lru_cache
def recurse(key):
    if conn[key][0]=="out":
        return 1
    else:
        r=0
        for new_key in conn[key]:
            r+=recurse(new_key)
        return r

print(recurse("you"))

# P2
conn=dict()

with open("input.txt") as ifile:
    for line in ifile:
        key,val = line.strip().split(": ")
        vals=val.split(" ")
        conn[key]=vals
print(conn)

from functools import lru_cache

@lru_cache
def recurse(key,fft,dac):
    if conn[key][0]=="out":
        return 1 if (fft and dac) else 0
    else:
        r=0
        for new_key in conn[key]:
            if new_key=="fft":
                r+=recurse(new_key,True,dac)
            elif new_key=="dac":
                r+=recurse(new_key,fft,True)
            else:
                r+=recurse(new_key,fft,dac)
        return r

print(recurse("svr",False,False))
