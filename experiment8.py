l1=[]
v=[]
iden = []
iden_dic={}
newop={}
op=[]
term=[]
import re
with open("new.txt","r") as file:
    line=file.read().splitlines()
    file.close()
for i in line:
    r=re.split("\s*",i)
    l1.append(r)
print(l1)
operator = {"/":10,"*":10,"+":5,"-":5,"$":1}
for i in range(0,len(l1)):
    for j in range(0,len(l1[i])):
        if l1[i][j].isupper():
            v.append(l1[i][j])

        else:
            if l1[i][j]!="=":
                term.append(l1[i][j])
            if l1[i][j].isalpha():
                iden.append(l1[i][j])
                iden_dic[l1[i][j]] = 100
            elif l1[i][j]!="=":
                op.append(l1[i][j])
newop.update(operator)
newop.update(iden_dic)
print("OPERATORS: ",op)
print("VARIABLE: ",set(v))
print("IDENTIFIER: ",iden)
term.append('$')
print("TERMINAL: ",term)

inp = input("Enter the string to check with space and add $ at end with space: ")
st = ["$"]
b=inp.split(" ")

num = True

print(str(st)+"\t",end="")
print(b)

while num:
    for i in range(0,len(b)):
        if (st[-1] == b[i]):
            print("STRING ACCEPTED")
            num = False
        else:
            if(newop.get(st[-1]) < newop.get(b[i])):
                st.append(b[i])
            elif(newop.get(st[-1]) > newop.get(b[i])) and newop.get(st[-1]!="$"):
                st.pop()
            else:
                num = False
            
