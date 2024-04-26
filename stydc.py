user_list= input('enter the elements specerate by space').split(' ')
print('user _list:',user_list)
#to determine step to reach a position
#x=int(input('enter the distance'))
#if(x<4):
    #print('first step')
#elif(x%4==0):
    #print(x/4)
#else:
    #print(x//4+1)
#to find the weight of the person     
a=int(input('enter the weight if the first person')) 
b=int(input('enter the weight of second person'))
years=0
while a<=b:
    a=a*3
    b=b*2
    years=years+1
print(years)    
    
  
    
