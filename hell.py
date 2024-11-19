# a number culculating program
def cal(n1,n2,sign):
    #to try and guess your operation 
    if sign == "-":
        return n1 -n2
    elif sign == "+":
        return n1+n2
    elif sign == "*":
        return n1 * n2 
    elif sign == "/":
        return n1/n2
    elif sign == "^":
        return n1**n2
    elif sign =="%":
        return n1%n2    
n1 = int(input("what is the first number"))
n2 = int(input("chose your second  number"))
sign = input("what is the operation you would like to perform ")   
answer = cal(n1,n2,sign)
print(answer)