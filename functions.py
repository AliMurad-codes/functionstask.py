f=input("First value:")
s=input("second value:")
choose=input("sum(f,s),sub(f,s),div(f,s),mul(f,s)")

def sum(f,s):
	answer = int(f)+int(s)
	return answer

def sub(f,s):
	answer=int(f)-int(s)
	return answer

def mul(f,s):
	answer =int(f)*int(s)
	return answer

def div(f,s):
	answer=int(f)/int(s)
	return answer

if choose == "sum":
	print("sum of two numbers:",sum(f,s))

elif choose =="sub":
	print("subtraction of two number:",sub(f,s))

elif choose =="div":
	print("div of number:",div(f,s))

elif choose =="mul":
	print("multiplication of two number:",mul(f,s))
else:
	print("wrong choose")