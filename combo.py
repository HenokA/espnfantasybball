with open ("data.txt","w") as f:
    f.write("1,2,3")#\10,20,30")

# store each line as list of words seperately    
lines = []
with open("data.txt") as f:
    for l in f:
        l = l.strip() # remove \n
        if l:
            lines.append( list(w.strip() for w in l.split(",")))
        for x in l.split(","):
            print(x)
            print(x*2.0)

print(lines) # [['red', 'green', 'blue'], ['banana', 'apple', 'orange']]

from itertools import combinations

with open("result.txt", "w") as f:
    for l in lines:
        for c in combinations(l,2):
            f.write(str(list(c)).replace("'","")) # remove the ' of strings
        f.write("\n")

print(open("result.txt").read())