#!/bin/python

# example string
s="11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
# input string
s="1090286-1131879,3259566-3404881,138124-175118,266204727-266361099,16765-24272,7657360692-7657593676,88857504-88926597,6869078-6903096,48444999-48532270,61427792-61580535,71-103,8077-10421,1920-2560,2-17,951-1259,34-50,28994-36978,1309-1822,9393918461-9393960770,89479-120899,834641-988077,5389718924-5389797353,34010076-34214499,5063-7100,607034-753348,19098586-19261191,125085556-125188689,39839-51927,3246-5037,174-260,439715-473176,187287-262190,348-535,58956-78301,4388160-4505757,512092-584994,13388753-13534387"


# Problem 1
# Note: interpretted it incorrectly first, thought any number repeating could cause invalid id
# e.g. 100 -> 2 zeros repeating: invalid. 10105 -> 10 10 repeating also invalid. That is what commented code would check
r=0
#invalid=False
for v in s.split(","):
    a,b = v.split("-")
    #print(a,b)
#    while int(a)<=int(b):
#        for i in range(1,len(a)//2+1):
#            for j in range(0,len(a)-(i*2)+1):
#                current=a[j:j+i]
#                next=a[j+i:j+2*i]
#                if current==next:
#                    print(current,a)
#                    r+=int(current)
#                    invalid=True
#                    break
#            if invalid:
#                break
                #print(a[j:j+i])
#        a=str(int(a)+1)
#        invalid=False
    while int(a)<=int(b):
        if a[:len(a)//2]==a[len(a)//2:]:
            r+=int(a)
            print(a)
        a=str(int(a)+1)

print(r)

# Problem 2
# Binary splitting the size instead of //2 -> up until //len(s) I guess? But with a set of all might be more interesting here

r=0
for v in s.split(","):
    a,b = v.split("-")
    for x in range(int(a),int(b)+1):
        x=str(x)
#        print("x: ", x)
        for i in range(1,(len(x)//2)+1):
#            print("i: ",i)
            uniques=set()
            for j in range(0,len(x),i):
                uniques.add(x[j:j+i])
            if len(uniques)==1:
                print(f"x: {x}, i: {i}")
                r+=int(x)
                break
            if x=="11":
                print(f"x: {x}, i: {i}")

print(r)
