# FUNCTION
def FirstFactorial(num):
	sum = num
	if num >=1 and num < 19 :
		while num > 1 :
			temp = num -1
			sum = sum * temp
			num = temp
		print("Output: \"" +  sum  + "\"")
	else:
		print("Invalid input...");

## ---------------------------------------- ##

# INTERFACE
print("Please input number between (1 - 18) : ")

try:
	num = int(input())
	FirstFactorial(num)
	#print(num)
except Exception as e:
	print("Invalid input...")