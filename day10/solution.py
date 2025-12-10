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
import heapq
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

        state=[0 for _ in range(len(power))]
#        print(state)
        to_test=[]
        for button in buttons:
            checked.add((tuple(state)))
            heapq.heappush(to_test,(0,state.copy(),button,0))
#        print(to_test)
        print(state,power)
        while True:
#            print(highest_key)
#            print(to_test)
#            print(checked)
            score,s,bu,n = heapq.heappop(to_test)
#            print(s,bu,n,hist)
#            print(score)
            overflow=False
            new_s=list(s)
            for i in bu:
                if (new_s[i]+1)> power[i]:
                    overflow=True
                new_s[i]+=1
            if overflow:
                continue
            n+=1
            tup_s=tuple(new_s)
            if new_s == power:
                break
            else:
                total_score=-sum(new_s)
#                print(total_score)
                if tup_s not in checked:
                    for button in buttons:
                            checked.add(tup_s)
                            heapq.heappush(to_test,(total_score/n,new_s,button,n))
#        print("fewest=",n)
        r+=n
print(r)
