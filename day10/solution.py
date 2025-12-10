print("P1")
r=0
with open("input.txt") as ifile:
    for line in ifile:
        checked=set()
        li,bu_pow=line.split("] ")
        lights=list(li[1:])
        bu,pow=bu_pow.split(" {")
        buttons_text=bu.split(" ")
        buttons=[]
        for bu_text in buttons_text:
            buttons.append(list(map(int,bu_text[1:-1].split(","))))
        power=list(map(int,pow[:-2].split(",")))
#        print(lights,buttons,power)

        state=["." for _ in range(len(lights))]
#        print(state)
        to_test=[]
        for button in buttons:
            checked.add((tuple(state.copy()),tuple(button)))
            to_test.append((state.copy(),button,0,[]))
#        print(to_test)
        while True:
            s,bu,n,hist = to_test.pop(0)
#            print(s,bu,n,hist)
            for b in bu:
                if s[b] == "#":
                    s[b]="."
                else:
                    s[b]="#"
            n+=1
            if s == lights:
                break
            else:
                hist.append(bu)
                for button in buttons:
                    if (tuple(s.copy()), tuple(button)) not in checked:
                        checked.add((tuple(s.copy()), tuple(button)))
                        to_test.append((s.copy(),button,n,hist.copy()))
#        print("fewest=",n)
        r+=n
print(r)

print("P2")
r=0
# Little bit cheaty to use linprog function

# Idea came from having a function approach:
# For example line 1 of test input you could write as:
# a(x+z+w) + b(y+w) + c(z+w) + d(x+y+z) + e(x) = 31x+4y+31z+29w
# Where x,y,z,w are irrelevant and we want to solve for a,b,c,d,e (times we press each button) so that the sum of them is the smallest
# and whole integers -> linear algebra solving in python can be done usint linprog from scipy =D

from scipy.optimize import linprog

with open("input.txt") as ifile:
    for line in ifile:
        checked=set()
        li,bu_pow=line.split("] ")
        lights=list(li[1:])
        bu,pow=bu_pow.split(" {")
        buttons_text=bu.split(" ")
        buttons=[]
        for bu_text in buttons_text:
            buttons.append(list(map(int,bu_text[1:-1].split(","))))
        power=list(map(int,pow[:-2].split(",")))
        print(lights,buttons,power)

        state=[[0 for _ in range(len(buttons))] for _ in range(len(power))]

        for i,button in enumerate(buttons):
            for p in button:
                state[p][i]=1
        print("matrix:",state)
        print(power)
        bounds = [(0, None) for _ in range(len(buttons))]

        c = [1 for _ in range(len(buttons))]
        res = linprog(c, A_eq=state, b_eq=power, bounds=bounds, method='highs', integrality=1)
        print(res.fun)
        r+=res.fun
print(r)
