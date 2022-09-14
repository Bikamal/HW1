x=int(input())
y=int(input())
z=int(input())

if(x==y and x==z and y==z):
    print("equilateral triangle ")
elif(x!=y and x!=z and y!=z):
    print("scalene triangle")
elif(x==y or x==z or y==z):
    print(" isosceles triangle")