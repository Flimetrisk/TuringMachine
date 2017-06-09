x = input("Dos numeros en sistema unario separado por un 0: ")
x = list(x)
pos = 0
valorMaq = 0
while (True):
	if valorMaq==0 and x[pos]=='0':
		valorMaq=0
		x[pos]='0'
		pos=pos+1
		print(x)

	elif valorMaq==0 and x[pos]=='1':
		valorMaq=11
		x[pos]='0'
		pos=pos-1
		print(x)

	elif valorMaq==1 and x[pos]=='0':
		valorMaq=10
		x[pos]='1'
		pos=pos+1
		print(x)

	elif valorMaq==1 and x[pos]=='1':
		valorMaq=1
		x[pos]='1'
		pos=pos-1
		print(x)
############################################
	elif valorMaq==10 and x[pos]=='0':
		valorMaq=1010
		x[pos]='0'
		pos=pos+1
		print(x)

	elif valorMaq==10 and x[pos]=='1':
		valorMaq=11
		x[pos]='0'
		pos=pos+1
		print(x)
	
	elif valorMaq==11 and x[pos]=='0':
		valorMaq=100
		x[pos]='0'
		pos=pos+1
		print(x)

	elif valorMaq==11 and x[pos]=='1':
		valorMaq=11
		x[pos]='1'
		pos=pos+1
		print(x)
#############################################
	elif valorMaq==100 and x[pos]=='0':
		valorMaq=100
		x[pos]='0'
		pos=pos+1
		print(x)

	elif valorMaq==100 and x[pos]=='1':
		valorMaq=101
		x[pos]='0'
		pos=pos+1
		print(x)

	elif valorMaq==101 and x[pos]=='0':
		valorMaq=111
		x[pos]='0'
		pos=pos-1
		print(x)

	elif valorMaq==101 and x[pos]=='1':
		valorMaq=110
		x[pos]='1'
		pos=pos-1
		print(x)

	elif valorMaq==110 and x[pos]=='0':
		valorMaq=110
		x[pos]='0'
		pos=pos-1
		print(x)

	elif valorMaq==110 and x[pos]=='1':
		valorMaq=1
		x[pos]='1'
		pos=pos-1
		print(x)

	elif valorMaq==111 and x[pos]=='0':
		valorMaq=111
		x[pos]='0'
		pos=pos-1
		print(x)

	elif valorMaq==111 and x[pos]=='1':
		valorMaq=1000
		x[pos]='1'
		pos=pos-1
		print(x)
################################################
	elif valorMaq==1000 and x[pos]=='0':
		valorMaq=1001
		x[pos]='0'
		pos=pos-1
		print(x)

	elif valorMaq==1000 and x[pos]=='1':
		valorMaq=1000
		x[pos]='1'
		pos=pos-1

	elif valorMaq==1001 and x[pos]=='0':
		valorMaq=10
		x[pos]='0'
		pos=pos+1
		print(x)

	elif valorMaq==1001 and x[pos]=='1':
		valorMaq=1
		x[pos]='1'
		pos=pos-1
		print(x)

	elif valorMaq==1010 and x[pos]=='1':
		valorMaq=1010
		x[pos]='1'
		pos=pos+1
		print(x)

	elif valorMaq==1010 and x[pos]=='0':
		valorMaq=0
		x[pos]='0'
		pos=pos+1
		break
		print(x)

x = ''.join(x)
print("Maximo comun divisor: ", x)
