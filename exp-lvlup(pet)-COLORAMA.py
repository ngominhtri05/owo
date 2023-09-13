#CREATEbyMHuong10
#DONEbyMTri885
#2.0
#CALCULATE-EXP-FOR-PET-OWO
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print("_____________________________________")
print(f"{Fore.WHITE}{Back.RED}NOTICE")
print(f"{Style.BRIGHT}     1{Style.NORMAL}:if your{Fore.YELLOW} Exp pet(K){Fore.WHITE}, {Fore.YELLOW}Exp per day(K) {Fore.WHITE}is a real number, use: .")
print(f"{Fore.BLUE}    Ex{Fore.WHITE}: Exp pet(K): 5.64 (for 5640 exp)")
print(f"{Style.BRIGHT}     2{Style.NORMAL}: your value must be a number")
print("_____________________________________")
print(f"{Fore.GREEN}Level pet: ")
x=float(input())
print(f'{Fore.YELLOW}Exp pet(K): ')
y=float(input())
print(f'{Fore.GREEN}Level you need: ')
z=float(input())
print(f'{Fore.YELLOW}Exp per day(K)-{Fore.CYAN}use default: 500(k)-{Fore.WHITE}TYPE:0 : ')
expperday=int(input())
print("_____________________________________")
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
if 0<x<=100 and x%1==0 and 0<=y and x<z<=100 and z%1==0 and expperday>=0:
	x=int(x)
	z=int(z)
	t=int(expr(x,z,y))
	if expperday==0:
		t2=t/500000
	else:
		t2=t/expperday/1000
	t4=t2/(365+1/4)
	t5=str(round(t4,3))
	print(f"{Fore.WHITE}{Back.RED}Exp needing{Fore.WHITE}{Back.BLACK}:{Fore.YELLOW}{Style.BRIGHT} "+exp(t)+f"{Style.NORMAL}{Fore.CYAN} xp")
	print(f"{Fore.WHITE}{Back.RED}ESTIMATed time{Fore.WHITE}{Back.BLACK}:{Fore.RED}{Style.BRIGHT}"+exp(int(t2))+','+str(int(t2%10))+ f"{Fore.CYAN}{Style.NORMAL} ngày = {Fore.RED}{Style.BRIGHT}"+t5+f"{Fore.CYAN}{Style.NORMAL} năm")
	print("_____________________________________")
else:
	while x<0 or x>100 or x%1!=0 or 0>y or z%1!=0 or expperday<0 or x>=z or z>100:
		print("_____________________________________")
		print(f'{Fore.WHITE}{Back.RED}ERROR VALUE ;-;')
		print(f"{Fore.GREEN}Level pet: ")
		x=float(input())
		print(f'{Fore.YELLOW}Exp pet(K): ')
		y=float(input())
		print(f'{Fore.GREEN}Level you need: ')
		z=float(input())
		print(f'{Fore.YELLOW}Exp per day(K)-{Fore.CYAN}use default: 500(k)-{Fore.WHITE}TYPE:0 :')
		expperday=int(input())
		print("_____________________________________")
	x=int(x)
	z=int(z)
	t=int(expr(x,z,y))
	if expperday==0:
		t2=t/500000
	else:
		t2=t/expperday/1000
	t4=t2/(365+1/4)
	t5=str(round(t4,3))
	print(f"{Fore.WHITE}{Back.RED}Exp needing{Fore.WHITE}{Back.BLACK}:{Fore.YELLOW}{Style.BRIGHT} "+exp(t)+ f"{Style.NORMAL}{Fore.CYAN} xp")
	print(f"{Fore.WHITE}{Back.RED}ESTIMATed time{Fore.WHITE}{Back.BLACK}:{Fore.RED}{Style.BRIGHT} "+exp(int(t2))+','+str(int(t2%10))+ f"{Fore.CYAN}{Style.NORMAL} ngày = {Fore.RED}{Style.BRIGHT}"+t5+f"{Fore.CYAN}{Style.NORMAL} năm")
	print("_____________________________________")
