#assignment
def accept():
    id = int(input("enter id:"))
    mnum = int(input("enter mobile number"))
    sal = int(input("enter salary:"))
    dsg = input("enter designation:")
    return sal, dsg, id,mnum
x, y, k, t = accept()
def cal():
    if y=="pm":
        if x>=80000:
            hike=x+(x*0.5)
        elif 80000<x and x>=60000:
            hike=x+(x*0.3)
        else:
            hike=x+(x*0.01)
    elif y=="tm":
        if x>=70000:
            hike=x+(x*0.5)
        elif 70000<x and x>=50000:
            hike=x+(x*0.3)
        else:
            hike=x+(x*0.01)
    elif y=="devl":
        if x>=85000:
            hike=x+(x*0.5)
        elif 85000<x and x>=60000:
            hike=x+(x*0.3)
        else:
            hike=x+(x*0.01)
    return hike
h=cal()
def display():
    print("id:",k)
    print("number:",t)
    print("designation:",y)
    print("salary:",x)
    print("hike in %:",((h-x)*100)/x)
    print("total salary:",h)
display()
#function:writing a repeated statements in block of statements in one programme and call n number of times is called functions
def first():
    a=input("enter one number:")
    b=input("enter second number:")
    c=int(a)+int(b)
    print(c)

first()
#one function we can call number times in whole programme
first()
first()

def  second():
    a=int(input("enter ur age"))
    if a>=18:
        print("ur eligible")
    else:
        print("ur not eligible")
second()
#global variables:we can write variable along the main line programme and we can use anyfunctons
n1=int(input("enter one number:"))
n2=int(input("enter one number:"))
def a1():
   n3=n1+n2
   print(n3)
def a2():
    n4=n1-n2
    print(n4)
a1()
a2()
#local variables:we can write these varibles inside the function we cant use these variables in anthorefunction
def b1():
    n1=int(input("enter one number"))
    n2=int(input("enter second number"))
    #n1,n2 are localvariables
    n3=n1+n2
    print(n3)
b1()
def b2():
    n3=n1+n2
    print(n3)
b2()#    n3=n1+n2
#NameError: name 'n1' is not defined
#passing arguments:
#1)positional arguments
def c1(a,b):
    c=a+b
    print(c)
c1(24,25)#the first value will be a and second value will be b we can say its positional because directly its assigning by positional
c1(24)#TypeError: c1() missing 1 required positional argument: 'b' u should pass as many requires to as many argumentes
#2)keyword arguments
def d1(a,b,c):
    print(a+b+c)
d1(a=100,b=200,c=300)
d1(100,b=200,c=300)
d1(100,200,c=300)
d1(100,b=300,c=400,a=120)#TypeError: d1() got multiple values for argument 'a'
d1(100,b=200,300)#SyntaxError: positional argument follows keyword argument but keyarument dosenot follows the positional argument
#3)default arguments:
#default argument should be in last not in first
def e1(a,b,c,d=0):
    e=a+b+c+d
    print(e)
e1(100,b=200,c=300)#if dosent give d value by default it will take d value as 0
e1(100,200,c=300,d=400)#if u take any value in d value dirctly it will take given value no  difalut value
#4)var length arguments:it can accept positonal arguments and it dosen't accept keyword and default arguments
def f1(a,b,*var):
    print(a)
    print(b)
    print(var)#it will give values in tuple format
f1(100,200,300,400,500,600,710,800,900)
def f2(*args):
    print(args)
f2(100,200,300,400,500)
def f2a(*args):#it dosen't take keywords arguments in *args
    print(args)
f2a(100,200,300,400,b=500)#TypeError: f2a() got an unexpected keyword argument 'b'
def f3(a,*var,b):#var f0llows only keyword arguments
    print(a)
    print(b)
    print(var)
f3(100,200,300,400,500)#TypeError: f3() missing 1 required keyword-only argument: 'b'
#5)keyword variable length argument:
def g1(*var,**a1):
    print(var)#it will store in the form of tuple
    print(a1)#it will store in the form of dictionary
g1(100,200,300,a=100,b=200,c=300)
def g2(*args,**kwargs):
    print(args)
    print(kwargs)
    list=[]
    s=0
    for i in args:
        list.append(i)
        s=s+i
    print(list)
    print(s)
    kwargs["d"]=400
    print(kwargs)
g2(100,200,300,a=100,b=200,c=300)
#return function:
def h1():
    n1=int(input("enter one number"))
    n2=int(input("enter second number"))
    n3=n1+n2
    return n3
x=h1()
print(x)
def h2():
    n1=20
    n2=30
    n3=n1+n2
    return n3
print(h2())
def h3(n1,n2):
    n3=n1+n2
    return n3
x=h3(5,6)
print(x)
def h4(n1,n2):
    n3=n1+n2
    return n3
print(h4(5,6))
def h5():
    a=11
    b=22
    c=33
    d=a+b+c
    return a,b,c,d
w,x,y,z=h5()
print(w,x,y,z,sep="\n")
def h6():
    a=11
    b=22
    c=33
    d=a+b+c
    return a,b,c,d
x,*y=h6()# *y will store in list format
print(x,y,sep="\n")
def h7():
    a=22
    b=33
    c=a+b
x=h7()
print(x)
def h5():
    a=11
    b=22
    c=33
    d=a+b+c
    return a,b,c,d
x=h5()#it will store in tuple format y cause returning values 3 but catching values only one variable
print(x)
#reference copy:if we create any function by default it will create one reference variable  as function name  in that  we have address of function
def teja():
    print("teja is practicing python coding")
teja()
r=teja#here we are coping adderess of the function in another variable
r()
#passing one function reference  to another function
def chandu(fun):
    print("cool")
    fun()
def raju():
    print("hot")
r=raju
chandu(r)
#whatever you give datatype it will store same as that datatype
def chandu(fun):
    print("cool")
    print(fun)
    print(type(fun))
chandu("teja")#<class 'str'>
chandu(10)#<class 'int'>
#nested function
def cnu():
    n1=int(input("enter one number:"))
    n2=int(input("enter second number:"))
    n3=n1+n2
    n4=n1-n2
    print(n3)
    print(n4)
    def vinod():#local variables we can use in nested function
        n5=n1*n2
        n6=n1/n2
        print(n5)
        print(n6)
    vinod()
cnu()
def cnu():
    n1=int(input("enter one number:"))
    n2=int(input("enter second number:"))
    n3=n1+n2
    print(n3)
    def vinod():#local variables we can use in nested function
        n5=n1*n2
        print(n5)
        def teja():
            n6 = n1 / n2
            print(n6)
            def raju():
                n4 = n1 - n2
                print(n3)
                def chandu():
                    print("all calculation have done")
                chandu()
            raju()
        teja()
    vinod()
cnu()
#clouser property:nested function reference is return to main program and run in the main line is called clouser property
def cnu():
    n1=int(input("enter one number:"))
    n2=int(input("enter second number:"))
    n3=n1+n2
    n4=n1-n2
    print(n3)
    print(n4)
    def vinod():#local variables we can use in nested function
        n5=n1*n2
        n6=n1/n2
        print(n5)
        print(n6)
    return vinod
x=cnu()
x()
#2)
def cnu():
    n1=int(input("enter one number:"))
    n2=int(input("enter second number:"))
    n3=n1+n2
    print(n3)
    def vinod():#local variables we can use in nested function
        n5=n1*n2
        print(n5)
        def teja():
            n6 = n1 / n2
            print(n6)
            def raju():
                n4 = n1 - n2
                print(n4)
                def chandu():
                    print("all calculation have done")
                return chandu
            r=raju()
            return r
        t=teja()
        return t
    v=vinod()
    return v
c=cnu()
c()
#decoraters
def deco_outer(func):
    def deco_inner():
        print("*********************************")
        func()
        print("currently dealing with decoretors")
        print("***************************************")
    return deco_inner
@deco_outer
def class1():
    print("teja is practising python programme")
class1()
#recursion:like infinite loop calling one funcion in same function
import time
def fun():
    print("hello")
    time.sleep(2)
    fun()
fun()
#2)
def rec(n):
    if n<1:
        return
    print(n)
    n=n-1
    rec(n)
rec(10)
#passing list and return two values and printing two values
a=input("enter 10 names:")
b=a.split()
print(b)
def name(b):
    above=0
    below=0
    for i in b:
        if len(i)>=5:
            above+=1
        else:
            below+=1
    return above,below
above,below=name(b)
print("above={} and below={}".format(above,below))





