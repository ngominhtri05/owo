s#1.0.4
#CALCULATE-EXP-FOR-PET
print("_____________________________________")
x=int(input('Level hiện tại: '))
y=int(input('Exp hiện tại (nghìn): '))
z=int(input('Level sau: '))
def exp(a):
    str1=str(a)
    str2=""
    c=len(str1)
    for i in range(1,c+1):
        b=a%10
        a=(a-b)/10
        str2=str(int(b))+str2
        if i%3 ==0 and i<c:
            str2="."+str2
    return str2
def expr(a,b,c):
    sum1=0
    for i in range(a,b,1):
        sum1=(1000+i**4)+sum1
        if i == b-1:
            sum1=sum1-c*1000
            return sum1
t=expr(x,z,y)
t2=t/500000
t4=t2/365
t5=str(round(t4,3))
print("Exp cần: "+exp(t))
print("Dự tính: "+exp(int(t2))+","+str(int(t2%10))+ " ngày = "+t5+" năm")
print("_____________________________________")
