 number =int(input('enter the value of number'))
sum=0
for i in range(1,number+1):
    sum+=i
    print('sum of frist',number,'natural numbers',sum)    
value=number*(number+1)/2
print(value)
number =int(input('enter the value of number'))
fact=1
for i in range(1,number+1):
    fact*=i
print('factorial',number,'is',fact)    
