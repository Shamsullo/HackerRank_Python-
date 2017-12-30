j = 0 
nested = []
for i in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    
    inner = []
    inner.append(name)
    inner.append(score)
    
    
    nested.insert(j, inner)
    j += 1
    
givengrades = sorted({x[1] for x in nested})
sts = sorted(x[0] for x in nested if x[1] == givengrades[1])
for s in sts:
    print(s)
    
#print min
    
        
