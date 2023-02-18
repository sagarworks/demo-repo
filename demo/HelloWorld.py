#Variable declaration
name = "Edureka"
f = 1991
print("python was founded in"  , f)
#data types
a = [1,2,3,4,5,6,7]
b = {1 : 'edureka' , 2: 'python'}
c = (1,2,3,4,5)
d = {1,2,3,4,5}
print("the list is" , a)
print("the dictionary is" , b)
print("the tuple is" , c)
print("the set is " , d)

#Operators
a = 10
b = 15
#arithmetic operator
print(a + b)
print(a - b)
print(a * b)
#assignment operator
a += 10
print(a)
#comparison operator
#a != 10
#b == a
#logical operator
a > b and a > 10
#this will return true if both the statements are true.


#Control Statements
name = 'edureka'
for i in name:
    if i == 'a':
        break
    else:
        print(i)
         
         
#Functions         
def func(a):
    return a ** a
res = func(10)
print(res)

#Classes And Objects
class Parent:
    def func(self):
        print('this is parent')
 
class Child(Parent):
    def func1(self):
        print('this is child')
 
#ob = new Child()
#ob.func()