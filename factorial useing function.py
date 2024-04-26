
number =int(input('enter the value of number'))
def factorial(number):
    
    fact=1
    for i in range(1,number+1):
        fact*=i
    return fact
result=factorial(number)
print(result)  
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input('enter the number'))  
print(factorial(n))     
        
  
