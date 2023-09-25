print('salam')
x=1
print(x)
z=2.2
print(z)
print(9)
x=3
print(x*3)
x=7
print(x*7)
pi=3.1415
r=6
print(pi*r*r)
masahat=pi*r*r
print(masahat)
x=1
x=x+1
print(x)
x_2=7
print(x_2)
gheymat_livan=100
tedad_livan=50
gheymat_kol=gheymat_livan*tedad_livan
print(gheymat_kol)
x=2
print(x**3)
print(2**4)
print(17//2)
print(17%2)
print(124%10)
print(124%100)
print(6*2-(4-2)**2)
myname='maryam'
myfamilyname='rafati'
print(myname)
print(myfamilyname)
print(myname+myfamilyname)
print(myname+" "+myfamilyname)
print(myname*3)
#age_1=input('please provide your age:')
#print(age_1)
#print(age_1*2)
#age_1=int(age_1)
#print(age_1*2)
#age_2=input('please provide your mother age:')
#print(age_2)
#print(har chi benevisi)
print(type(3))
print(type('hello'))
print(type(False))
print(5+5)
#print(5>4)
#print(10>14)
a=3
b=-3
#print(a>b)
a=6
b=5
print(a==b)
print(a!=b)
print(a<=b)
print((a>b)and(a==6))
print((2<3)and(5<10))
print((2<3)or(5<2))
print(not(a<=b))
x=50
if x%2==0:
    print('zoj')
else:
    print('fard')

x=41
if x%2==0:
    print('be 2')
elif x%3==0:
    print('be 3')
else:
    print('na be 2 na be 3')

name=input('please provide your name:')
if name=='maryam':
    print('salam maryam')
elif name=='jadi':
    print('salam jadi')
else:
    print('salam gharibe')

#build in function
print('hello')
print(type(2))
print(max('512'))
print(max('sara'))

#library function
import math
print(math.sin(0.5))
import random
print(random.random())
import random
print(random.randint(10,20))
from random import randint
print(randint(2,10))
import datetime
print(datetime.date.today())
print(datetime.datetime.now().strftime("%y-%m-%d"))
print(datetime.datetime.now().strftime("%y%m%d"))
print(type(datetime.datetime.now().strftime("%y%m%d")))

#self function
def salambye():
    print('salam')
    print('byebye')
print('shoroo') 
salambye()
print('tamoom')


def salambye(name):
    print('salam',name)
    print('bye bye',name)
salambye('maryam')
salambye('mobina')

def jam(a,b):
    javab=a+b
    return (javab) 
print(jam(2,3))

def jam(c,d):
    javabe=c+d
    return javabe
adade_aval=2
adade_dovvom=1
jam_2_adad=jam(adade_aval,adade_dovvom)
print(jam_2_adad)

def hoghoogh(hour,per_hour):
    if hour>8:
        return 'error! too much work!'
    elif hour<7:
        return 'do not work!'
    else:
        kolle_daramad=hour*per_hour
        return kolle_daramad
print(hoghoogh(5,2))


n=5
while n>0:
    print(n)
    n=n-1

name=input('what is your name?')
while name!='end':
    print('salam',name)
    name=input('what is your name?')


m=10
while m>=0:
    print(m)
    m=m+1
    if m==100:
        print('ohh you reach 100')
        break
print('out of the loop')




n=5
while n>0:
    print(n)
    n=n-1

for i in range(1,10):
    print(i)


for i in range(1,10):
    print(i,i*i)
    if i==5:
        print('you reach 5!')
        break  

friends=['h','hh','hhh']
count=0
for v in friends:
    print('salam',v)
    count=count+1
print('I said',count,'hellos')


guess=input('please enter your guess:')
guess=int(guess)
sum=0
n=0
while guess!=-1:
    sum=guess+sum
    n=n+1
    guess=input('please enter your guess:')
    guess=int(guess)
    if guess==-1:
        print(sum/n)















