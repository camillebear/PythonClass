name = input("enter your name : ")
print ('hello '+ name )
x = 10 
print (x)
n = int(input("enter a number : "))
if n < 10:
    print('Your number is less than 10!')
elif n > 10: 
    print('Your number in greater than 10!')
elif n == 10: 
    print('Your number is equal to 10!')
p = int(input("enter a number : "))
if p% 2 == 1: 
    print('This number is odd.')
else:
    print('This number is even.')

food = ['chocolate', 'water', 'juice'] 

for index in food:
    print(index)
numbers = []
for x in range(0,9):
    numbers.append(x)
print(numbers)