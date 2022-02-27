#QUESTION 1:
def towerofhanoi(n,source,helper,destination):
    if n==1:
        print("transfer of disk ",n," from ",source," to ",destination)
        return
    towerofhanoi(n-1,source,destination,helper)
    print("transfer of disk ",n," from ",source," to ",destination)
    towerofhanoi(n-1,helper,source,destination)
n=3
towerofhanoi(3,"S","H","D")

#QUESTION 2:
print("USING ITERATION")
n=int(input("ENTER NO. OF ROWS"))
L=[]
for i in range(n):
    r=[]
    for j in range(i+1):
        if j==0 or j==i:
            r.append(1)
        else:
            r.append(L[i-1][j-1] + L[i-1][j])
    L.append(r)

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(L[i][j],end=" ")
    print()
    
print("USING RECURSION")
def pascaltriangle(n):
    if n==0:
        return []
    elif n==1:
        return[[1]]
    newrow=[1]
    rowlist=pascaltriangle(n-1)
    lastrow=rowlist[-1]
    for i in range(len(lastrow)-1):
        num = lastrow[i] + lastrow[i+1]
        newrow.append(num)
    newrow.append(1)
    rowlist.append(newrow)
    return rowlist

n=int(input("ENTER NO. OF ROWS"))
L=pascaltriangle(n)
for i in range(n):
    for j in range(i+1):
        print(L[i][j],end=" ")
    print()
    
#QUESTION 3:
def quotientandremainder(dividend,divisor):
    print("FUNCTION TO FIND REMAINDER AND QUOTIENT CALLED")
    if(dividend>0 and divisor>0):
        q=dividend/divisor
        r=dividend%divisor
        print("QUOTIENT=",q)
        print("REMAINDER=",r)
        L=[]
        for i in (4,5,6):
            nq=q+i
            nr=r+i
            if nq>4:
                L.append(nq)
            if nr>4:
                L.append(nr)
        set(L)
        immutableset=frozenset(L)
        _max_=max(L)
        print("HASH VALUE OF MAX VALUE OF SET = ",hash(_max_))
        return
    else:
        print("INVALID INPUT,ONLY NON-ZERO VALUES ALLOWED")
        return
        
a=int(input("ENTER DIVIDEND"))
b=int(input("ENTER DIVISOR"))
quotientandremainder(a,b)


#QUESTION 4:
class Student:
    def __init__(self,name,rollnumber):
        self.name=name
        self.rollnumber=rollnumber
        print("new Student object created")
S1=Student("abc",123)
del S1
print("object S1 deleted successfully")

#QUESTION 5:
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
E1=Employee("Mehak",40000)
E2=Employee("Ashok",50000)
E3=Employee("Viren",60000)
print("3 new Employee objects successfully")
E1.salary=70000
print("salary attribute of object E1 updated successfully")
del E3
print("object E3 deleted successfully")

#QUESTION 6:
from nltk.corpus import words
print("WELCOME TO TEST YOUR FRIENDSHIP GAME")
g=input("GEORGE,ENTER YOUR WORD:")
for i in g:
    print(i,end=",")

print()    
b=input("BARBIE,ENTER A MEANINGFUL WORD MADE FROM THE ABOVE LETTERS AND SAME WORD OF GEORGE NOT ALLOWED")
if b in words.words():
    print("CONGRATULATIONS,CORRECT ANSWER")
    print("YOUR FRIENDSHIP IS TRUE")
else:
    print("OOPS,WRONG ANSWER")
    print("YOUR FRIENDSHIP IS FAKE")




















        

    
