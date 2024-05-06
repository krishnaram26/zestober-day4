a1 = int(input())
b2 = int(input())
c3 = int(input())

if a1 > b2 and b2 > c3 or a1 < b2 and b2 < c3: # prob of "B" being the 2nd highest num
    print(b2)
elif a1 > b2 and a1 < c3 or a1 < b2 and a1 > c3: # prob of "A" being the 2nd highest num
    print(a1)
elif c3 > a1 and c3 < b2 or c3 < a1 and c3 > b2: # prob of "C" being the 2nd highest num
    print(c3)