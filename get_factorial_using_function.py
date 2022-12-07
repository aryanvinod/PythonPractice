#factorial of a given number
def fact(num):
    result=1
    if num==0:
        print("Factorial of",num,"is 1")
    elif num<0:
        print("Factorial cannot defined for Negative values.")
    else:
        for i in range(num,0,-1):
            result=i*result
        print(result)
n=eval(input("Enter a Number:"))
fact(n)
