with open('output1.txt') as f:
    p = f.read()

with open('output2.txt') as j:
    q = j.read()

if p == q:
    print("identical")
else:
    print("Not identical ")