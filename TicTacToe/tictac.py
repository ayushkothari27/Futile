def checkwinuser(l1,l2,l3,user):
	if user>=3: 
		if l1[0] == l1[1] and l1[1] == l1[2] and l1[0]=="X":
			return 1;
		elif l2[0] == l2[1] and l2[1] == l2[2] and l2[0]=="X":
			return 1;
		elif l3[0] == l3[1] and l3[1] == l3[2] and l3[0]=="X":
			return 1;
		elif l1[0] == l2[0] and l2[0] == l3[0] and l1[0]=="X":
			return 1;
		elif l1[1] == l2[1] and l2[1] == l3[1] and l1[1]=="X":
			return 1;
		elif l1[2] == l2[2] and l2[2] == l3[2] and l1[2]=="X":
			return 1;
		elif l1[0] == l2[1] and l2[1] == l3[2] and l1[0]=="X":
			return 1;
		elif l1[2] == l2[1] and l2[1] == l3[0] and l1[2]=="X":
			return 1;
		else:
			return 0
	else:
		return 0;

def checkwincomp(l1,l2,l3,comp):
	if comp>=3: 
		if l1[0] == l1[1] and l1[1] == l1[2] and l1[0]=="O":
			return 1;
		elif l2[0] == l2[1] and l2[1] == l2[2] and l2[0]=="O":
			return 1;
		elif l3[0] == l3[1] and l3[1] == l3[2] and l3[0]=="O":
			return 1;
		elif l1[0] == l2[0] and l2[0] == l3[0] and l1[0]=="O":
			return 1;
		elif l1[1] == l2[1] and l2[1] == l3[1] and l1[1]=="O":
			return 1;
		elif l1[2] == l2[2] and l2[2] == l3[2] and l1[2]=="O":
			return 1;
		elif l1[0] == l2[1] and l2[1] == l3[2] and l1[0]=="O":
			return 1;
		elif l1[2] == l2[1] and l2[1] == l3[0] and l1[2]=="O":
			return 1;
		else:
			return 0
	else:
		return 0;
	

import random
l1=[" "," "," "]
l2=[" "," "," "]
l3=[" "," "," "]
print(l1)
print(l2)
print(l3)
user=0
comp=0
k=0
ch=random.randint(0,1)
print("Enter Choice between 0 and 1")
z=int(input())
if ch==z:
	print("User goes 1st")
	for i in range(0,4):
		print("Enter the list number and index. List number between 1-3 and index between 0-2")
		while 1>0:
			x=int(input())
			y=int(input())
			if x==1:
				if l1[y]!=" ":
					print("Space already filled")
					continue
			elif x==2:
				if l2[y]!=" ":
					print("Space already filled")
					continue
			else:
				if l3[y]!=" ":
					print("Space already filled")
					continue
			if x==1:
				l1[y]="X"
				user=user+1
				break
			elif x==2:
				l2[y]="X"
				user=user+1
				break
			else:
				l3[y]="X"
				user=user+1
				break
		print(l1)
		print(l2)
		print(l3)
		print()
		k=checkwinuser(l1,l2,l3,user)
		if k==1:
			print("user wins")
			break
		while 1>0:
			if (l1[0]=='X' and l2[1]==' ' and user==1) or (l1[2]=='X' and l2[1]==' ' and user==1) or (l3[0]=='X' and l2[1]==' ' and user==1) or (l3[2]=='X' and l2[1]==' ' and user==1):
				x=2
				y=1
				break
			elif l1[1]=='X' and user==1:
				x=2
				y=1
				break
			elif l2[0]=='X' and user==1:
				x=2
				y=1
				break
			elif l2[2]=='X' and user==1:
				x=2
				y=1
				break
			elif l3[1]=='X' and user==1:
				x=2
				y=1
				break
			elif l2[1]=='X' and l1[2]==' ' and user==1:
				x=1
				y=2
				break
			elif l1[0]=='X' and l2[1]=='O' and l3[2]=='X' and user==2:#corner1
				x=1
				y=1
				break
			elif l1[2]=='X' and l2[1]=='O' and l3[0]=='X' and user==2:
				x=1
				y=1
				break
			elif l2[1]=='X' and l1[2]=='O' and l3[0]=='X'and user==2:#center1
				x=3
				y=2
				break
			elif l1[0]=='O' and l1[1]=='O' and l1[2]==' ': #1
				x=1
				y=2
				break
			elif l1[0]=='O' and l1[2]=='O' and l1[1]==' ':
				x=1
				y=1
				break
			elif l1[1]=='O' and l1[2]=='O' and l1[0]==' ':
				x=1
				y=0
				break
			elif l2[1]=='O' and l2[2]=='O' and l2[0]==' ': #4
				x=2
				y=0
				break
			elif l2[0]=='O' and l2[2]=='O' and l2[1]==' ':
				x=2
				y=1
				break
			elif l2[0]=='O' and l2[1]=='O' and l2[2]==' ':
				x=2
				y=2
				break
			elif l3[0]=='O' and l3[2]=='O' and l3[1]==' ':
				x=3
				y=1
				break
			elif l3[0]=='O' and l3[1]=='O' and l3[2]==' ': #8
				x=3
				y=2
				break
			elif l3[1]=='O' and l3[2]=='O' and l3[0]==' ':
				x=3
				y=0
				break	
			elif l1[0]=='O' and l2[0]=='O' and l3[0]==' ':
				x=3
				y=0
				break
			elif l2[0]=='O' and l3[0]=='O' and l1[0]==' ':
				x=1
				y=0
				break
			elif l3[0]=='O' and l1[0]=='O' and l2[0]==' ':#12
				x=2
				y=0
				break
			elif l1[1]=='O' and l2[1]=='O' and l3[1]==' ':
				x=3
				y=1
				break
			elif l2[1]=='O' and l3[1]=='O' and l1[1]==' ':
				x=1
				y=1
				break
			elif l3[1]=='O' and l1[1]=='O' and l2[1]==' ':
				x=2
				y=1
				break		
			elif l1[2]=='O' and l2[2]=='O' and l3[2]==' ': #16
				x=3
				y=2
				break
			elif l2[2]=='O' and l3[2]=='O' and l1[2]==' ':
				x=1
				y=2
				break
			elif l3[2]=='O' and l1[2]=='O' and l2[2]==' ':
				x=2
				y=2
				break	
			elif l1[0]=='O' and l2[1]=='O' and l3[2]==' ':
				x=3
				y=2
				break
			elif l3[2]=='O' and l2[1]=='O' and l1[0]==' ': #20
				x=1
				y=0
				break
			elif l1[0]=='O' and l3[2]=='O' and l2[1]==' ':
				x=2
				y=1
				break	
			elif l1[2]=='O' and l2[1]=='O' and l3[0]==' ':
				x=3
				y=0
				break
			elif l1[2]=='O' and l3[0]=='O' and l2[1]==' ':
				x=2
				y=1
				break
			elif l2[1]=='O' and l3[0]=='O' and l1[2]==' ': #24
				x=1
				y=2
				break
			elif l1[0]=='X' and l1[1]=='X' and l1[2]==' ': #1
				x=1
				y=2
				break
			elif l1[0]=='X' and l1[2]=='X' and l1[1]==' ':
				x=1
				y=1
				break
			elif l1[1]=='X' and l1[2]=='X' and l1[0]==' ':
				x=1
				y=0
				break
			elif l2[1]=='X' and l2[2]=='X' and l2[0]==' ': #4
				x=2
				y=0
				break
			elif l2[0]=='X' and l2[2]=='X' and l2[1]==' ':
				x=2
				y=1
				break
			elif l2[0]=='X' and l2[1]=='X' and l2[2]==' ':
				x=2
				y=2
				break
			elif l3[0]=='X' and l3[2]=='X' and l3[1]==' ':
				x=3
				y=1
				break
			elif l3[0]=='X' and l3[1]=='X' and l3[2]==' ': #8
				x=3
				y=2
				break
			elif l3[1]=='X' and l3[2]=='X' and l3[0]==' ':
				x=3
				y=0
				break	
			elif l1[0]=='X' and l2[0]=='X' and l3[0]==' ':
				x=3
				y=0
				break
			elif l2[0]=='X' and l3[0]=='X' and l1[0]==' ':
				x=1
				y=0
				break
			elif l3[0]=='X' and l1[0]=='X' and l2[0]==' ': #12
				x=2
				y=0
				break
			elif l1[1]=='X' and l2[1]=='X' and l3[1]==' ':
				x=3
				y=1
				break
			elif l2[1]=='X' and l3[1]=='X' and l1[1]==' ':
				x=1
				y=1
				break
			elif l3[1]=='X' and l1[1]=='X' and l2[1]==' ':
				x=2
				y=1
				break		
			elif l1[2]=='X' and l2[2]=='X' and l3[2]==' ': #16
				x=3
				y=2
				break
			elif l2[2]=='X' and l3[2]=='X' and l1[2]==' ':
				x=1
				y=2
				break
			elif l3[2]=='X' and l1[2]=='X' and l2[2]==' ':
				x=2
				y=2
				break	
			elif l1[0]=='X' and l2[1]=='X' and l3[2]==' ':
				x=3
				y=2
				break
			elif l3[2]=='X' and l2[1]=='X' and l1[0]==' ': #20
				x=1
				y=0
				break
			elif l1[0]=='X' and l3[2]=='X' and l2[1]==' ':
				x=2
				y=1
				break	
			elif l1[2]=='X' and l2[1]=='X' and l3[0]==' ':
				x=3
				y=0
				break
			elif l1[2]=='X' and l3[0]=='X' and l2[1]==' ':
				x=2
				y=1
				break
			elif l2[1]=='X' and l3[0]=='X' and l1[2]==' ': #24
				x=1
				y=2
				break
			x=random.randint(1, 3)
			y=random.randint(0, 2)
			if x==1:
				if l1[y]=='X' or l1[y]=='O':
					continue
				else:
					print(x)
					print(y)
					break
			elif x==2:
				if l2[y]=='X' or l2[y]=='O':
					continue
				else:
					print(x)
					print(y)
					break
			elif x==3:
				if l3[y]=='X' or l3[y]=='O':
					continue
				else:
					print(x)
					print(y)
					break
		if x==1:
			l1[y]="O"
			comp=comp+1
		elif x==2:
			l2[y]="O"
			comp=comp+1
		else:
			l3[y]="O"
			comp=comp+1
		print(l1)
		print(l2)
		print(l3)
		print()	
		k=checkwincomp(l1,l2,l3,comp)
		if k==1:
			print("Computer wins")
			break	
	if k== 0:
		print("Enter the list number and index. List number between 1-3 and index between 0-2")
		x=int(input())
		y=int(input())
		if x==1:
			l1[y]="X"
			user=user+1
		elif x==2:
			l2[y]="X"
			user=user+1
		else:
			l3[y]="X"
			user=user+1
		print(l1)
		print(l2)
		print(l3)
		print()
		k=checkwinuser(l1,l2,l3,user)
		if k==1:
			print("user wins")
		else:
			print("Tie")
else:
	print("Computer goes 1st")
	for i in range(0,5):
		while 1>0:
			if comp==0:
				x=2
				y=1
				break
			elif l1[1]=="O" and l2[1]=="X" and comp==1:
				x=3
				y=2
				break
			elif l2[0]=="O" and l2[1]=="X" and comp==1:
				x=3
				y=2
				break
			elif l2[2]=="O" and l2[1]=="X" and comp==1:
				x=1
				y=0
				break
			elif l3[1]=="O" and l2[1]=="X" and comp==1:
				x=1
				y=0
				break
			elif l1[2]=="O" and l2[1]=="X" and comp==1:
				x=3
				y=0
				break
			elif l1[0]=="O" and l2[1]=="X" and comp==1:
				x=3
				y=2
				break
			elif l3[0]=="O" and l2[1]=="X" and comp==1:
				x=1
				y=2
				break
			elif l3[2]=="O" and l2[1]=="X" and comp==1:
				x=1
				y=0
				break
			elif comp==2 and user==2 and l3[0]=='X' and l2[1]=='X' and l1[2]=='O' and l1[0]==' ' and l3[2]==' ' and l3[1]=="O": #1
				x=1
				y=0
				break
			elif comp==2 and user==2 and l3[0]=='X' and l2[1]=='X' and l1[2]=='O' and l1[0]==' ' and l3[2]==' ' and l1[1]=="O":
				x=1
				y=0
				break
			elif comp==2 and user==2 and l3[0]=='X' and l2[1]=='X' and l1[2]=='O' and l1[0]==' ' and l3[2]==' ' and l2[0]=="O":
				x=3
				y=2
				break
			elif comp==2 and user==2 and l3[0]=='X' and l2[1]=='X' and l1[2]=='O' and l1[0]==' ' and l3[2]==' ' and l2[2]=="O": #4
				x=3
				y=2
				break
			elif comp==2 and user==2 and l3[0]=='O' and l2[1]=='X' and l1[2]=='X' and l1[0]==' ' and l3[2]==' ' and l3[1]=="O": #1 
				x=1
				y=0
				break
			elif comp==2 and user==2 and l3[0]=='O' and l2[1]=='X' and l1[2]=='X' and l1[0]==' ' and l3[2]==' ' and l1[1]=="O":  
				x=1
				y=0
				break
			elif comp==2 and user==2 and l3[0]=='O' and l2[1]=='X' and l1[2]=='X' and l1[0]==' ' and l3[2]==' ' and l2[0]=="O": 
				x=3
				y=2
				break
			elif comp==2 and user==2 and l3[0]=='O' and l2[1]=='X' and l1[2]=='X' and l1[0]==' ' and l3[2]==' ' and l2[2]=="O": #4
				x=3
				y=2
				break
			elif comp==2 and user==2 and l1[0]=='X' and l2[1]=='X' and l3[2]=='O' and l3[0]==' ' and l1[2]==' ' and l3[1]=="O": #1
				x=3
				y=0
				break
			elif comp==2 and user==2 and l1[0]=='X' and l2[1]=='X' and l3[2]=='O' and l3[0]==' ' and l1[2]==' ' and l1[1]=="O": 
				x=3
				y=0
				break
			elif comp==2 and user==2 and l1[0]=='X' and l2[1]=='X' and l3[2]=='O' and l3[0]==' ' and l1[2]==' ' and l2[0]=="O": 
				x=1
				y=2
				break
			elif comp==2 and user==2 and l1[0]=='X' and l2[1]=='X' and l3[2]=='O' and l3[0]==' ' and l1[2]==' ' and l2[2]=="O": #4
				x=1
				y=2
				break	
			elif comp==2 and user==2 and l1[0]=='O' and l2[1]=='X' and l3[2]=='X' and l3[0]==' ' and l1[2]==' ' and l3[1]=="O": #1
				x=3
				y=0
				break
			elif comp==2 and user==2 and l1[0]=='O' and l2[1]=='X' and l3[2]=='X' and l3[0]==' ' and l1[2]==' ' and l1[1]=="O": 
				x=3
				y=0
				break
			elif comp==2 and user==2 and l1[0]=='O' and l2[1]=='X' and l3[2]=='X' and l3[0]==' ' and l1[2]==' ' and l2[0]=="O": 
				x=1
				y=2
				break
			elif comp==2 and user==2 and l1[0]=='O' and l2[1]=='X' and l3[2]=='X' and l3[0]==' ' and l1[2]==' ' and l2[2]=="O": #4
				x=1
				y=2
				break
			elif l1[0]=='X' and l1[1]=='X' and l1[2]==' ': #1
				x=1
				y=2
				break
			elif l1[0]=='X' and l1[2]=='X' and l1[1]==' ':
				x=1
				y=1
				break
			elif l1[1]=='X' and l1[2]=='X' and l1[0]==' ':
				x=1
				y=0
				break
			elif l2[1]=='X' and l2[2]=='X' and l2[0]==' ': #4
				x=2
				y=0
				break
			elif l2[0]=='X' and l2[2]=='X' and l2[1]==' ':
				x=2
				y=1
				break
			elif l2[0]=='X' and l2[1]=='X' and l2[2]==' ':
				x=2
				y=2
				break
			elif l3[0]=='X' and l3[2]=='X' and l3[1]==' ':
				x=3
				y=1
				break
			elif l3[0]=='X' and l3[1]=='X' and l3[2]==' ': #8
				x=3
				y=2
				break
			elif l3[1]=='X' and l3[2]=='X' and l3[0]==' ':
				x=3
				y=0
				break	
			elif l1[0]=='X' and l2[0]=='X' and l3[0]==' ':
				x=3
				y=0
				break
			elif l2[0]=='X' and l3[0]=='X' and l1[0]==' ':
				x=1
				y=0
				break
			elif l3[0]=='X' and l1[0]=='X' and l2[0]==' ':#12
				x=2
				y=0
				break
			elif l1[1]=='X' and l2[1]=='X' and l3[1]==' ':
				x=3
				y=1
				break
			elif l2[1]=='X' and l3[1]=='X' and l1[1]==' ':
				x=1
				y=1
				break
			elif l3[1]=='X' and l1[1]=='X' and l2[1]==' ':
				x=2
				y=1
				break		
			elif l1[2]=='X' and l2[2]=='X' and l3[2]==' ': #16
				x=3
				y=2
				break
			elif l2[2]=='X' and l3[2]=='X' and l1[2]==' ':
				x=1
				y=2
				break
			elif l3[2]=='X' and l1[2]=='X' and l2[2]==' ':
				x=2
				y=2
				break	
			elif l1[0]=='X' and l2[1]=='X' and l3[2]==' ':
				x=3
				y=2
				break
			elif l3[2]=='X' and l2[1]=='X' and l1[0]==' ': #20
				x=1
				y=0
				break
			elif l1[0]=='X' and l3[2]=='X' and l2[1]==' ':
				x=2
				y=1
				break	
			elif l1[2]=='X' and l2[1]=='X' and l3[0]==' ':
				x=3
				y=0
				break
			elif l1[2]=='X' and l3[0]=='X' and l2[1]==' ':
				x=2
				y=1
				break
			elif l2[1]=='X' and l3[0]=='X' and l1[2]==' ': #24
				x=1
				y=2
				break
			elif l1[0]=='O' and l1[1]=='O' and l1[2]==' ': #1
				x=1
				y=2
				break
			elif l1[0]=='O' and l1[2]=='O' and l1[1]==' ':
				x=1
				y=1
				break
			elif l1[1]=='O' and l1[2]=='O' and l1[0]==' ':
				x=1
				y=0
				break
			elif l2[1]=='O' and l2[2]=='O' and l2[0]==' ': #4
				x=2
				y=0
				break
			elif l2[0]=='O' and l2[2]=='O' and l2[1]==' ':
				x=2
				y=1
				break
			elif l2[0]=='O' and l2[1]=='O' and l2[2]==' ':
				x=2
				y=2
				break
			elif l3[0]=='O' and l3[2]=='O' and l3[1]==' ':
				x=3
				y=1
				break
			elif l3[0]=='O' and l3[1]=='O' and l3[2]==' ': #8
				x=3
				y=2
				break
			elif l3[1]=='O' and l3[2]=='O' and l3[0]==' ':
				x=3
				y=0
				break	
			elif l1[0]=='O' and l2[0]=='O' and l3[0]==' ':
				x=3
				y=0
				break
			elif l2[0]=='O' and l3[0]=='O' and l1[0]==' ':
				x=1
				y=0
				break
			elif l3[0]=='O' and l1[0]=='O' and l2[0]==' ': #12
				x=2
				y=0
				break
			elif l1[1]=='O' and l2[1]=='O' and l3[1]==' ':
				x=3
				y=1
				break
			elif l2[1]=='O' and l3[1]=='O' and l1[1]==' ':
				x=1
				y=1
				break
			elif l3[1]=='O' and l1[1]=='O' and l2[1]==' ':
				x=2
				y=1
				break		
			elif l1[2]=='O' and l2[2]=='O' and l3[2]==' ': #16
				x=3
				y=2
				break
			elif l2[2]=='O' and l3[2]=='O' and l1[2]==' ':
				x=1
				y=2
				break
			elif l3[2]=='O' and l1[2]=='O' and l2[2]==' ':
				x=2
				y=2
				break	
			elif l1[0]=='O' and l2[1]=='O' and l3[2]==' ':
				x=3
				y=2
				break
			elif l3[2]=='O' and l2[1]=='O' and l1[0]==' ': #20
				x=1
				y=0
				break
			elif l1[0]=='O' and l3[2]=='O' and l2[1]==' ':
				x=2
				y=1
				break	
			elif l1[2]=='O' and l2[1]=='O' and l3[0]==' ':
				x=3
				y=0
				break
			elif l1[2]=='O' and l3[0]=='O' and l2[1]==' ':
				x=2
				y=1
				break
			elif l2[1]=='O' and l3[0]=='O' and l1[2]==' ': #24
				x=1
				y=2
				break
			x=random.randint(1, 3)
			y=random.randint(0, 2)
			if x==1:
				if l1[y]=='X' or l1[y]=='O':
					continue
				else:
					print(x)
					print(y)
					break
			elif x==2:
				if l2[y]=='X' or l2[y]=='O':
					continue
				else:
					print(x)
					print(y)
					break
			elif x==3:
				if l3[y]=='X' or l3[y]=='O':
					continue
				else:
					print(x)
					print(y)
					break
		if x==1:
			l1[y]="X"
			comp=comp+1
		elif x==2:
			l2[y]="X"
			comp=comp+1
		else:
			l3[y]="X"
			comp=comp+1
		print(l1)
		print(l2)
		print(l3)
		print()	
		k=checkwinuser(l1,l2,l3,comp)
		if k==1:
			print("Computer wins")
			break
		if comp==5:
			break
		print("Enter the list number and index. List number between 1-3 and index between 0-2")
		while 1>0:
			x=int(input())
			y=int(input())
			if x==1:
				if l1[y]!=" ":
					print("Space already filled")
					continue
			elif x==2:
				if l2[y]!=" ":
					print("Space already filled")
					continue
			else:
				if l3[y]!=" ":
					print("Space already filled")
					continue
			if x==1:
				l1[y]="O"
				user=user+1
				break
			elif x==2:
				l2[y]="O"
				user=user+1
				break
			else:
				l3[y]="O"
				user=user+1
				break
		print(l1)
		print(l2)
		print(l3)
		print()
		k=checkwincomp(l1,l2,l3,user)
		if k==1:
			print("user wins")
			break
