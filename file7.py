#Eg 4: To read all lines into list:
f=open("abcd.txt",'r')
lines=f.readlines()
for line in lines:
    print(line,end='')
f.close()