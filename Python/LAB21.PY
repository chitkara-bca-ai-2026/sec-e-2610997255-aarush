f=open("data.txt","w")
f.write("hhh")
f.close()
f =open("data.txt","r")

lines=0
words=0
chars=0

for line in f:
    line=line[:-1]
    lines+=1
    charsinline=len(line)
    chars+=charsinline
    w=len(line.split())
    words+=w
print(lines,words,chars)
f.close()
