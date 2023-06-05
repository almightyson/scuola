import math
string="tiamo"
key="bla"
row=len(string)/len(key)
resto=len(string)%len(key)
Row=math.ceil(row)
culumn=len(key)

i=0
while i<resto:

    string=string+"#"
    i=i+1
print(string)

a=[] 
nl=0
for x in range(Row):
    b=[]
    for y in range(culumn):
        valore=string[nl]
        b.insert(y,valore)
        nl=nl+1
        
    a.insert(x,b)
print(a)


a1=[]
nl=0
for x in range(len(key)):
    b1=[]
    for y in range(len(a)):
        valore=a[y][x]
        b1.insert(y,valore)
        
    a1.insert(x,b1)
print(a1)

a2=sorted(a1, key=lambda x: x[0])
print(a2)


a3=""
for x in range(len(key)):
    for y in range(len(a)):
        let=a2[x][y]
        a3 += let

print(a3)    
    
