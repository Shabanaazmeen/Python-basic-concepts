n=int(input('enter the number of terms'))
a,b=0,1
for _ in range(n):
    print(a,end=' ')
    #a,b=b,a+b
    temp_a=a
    a=b
    b=temp_a+b
    

