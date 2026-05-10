#--Swapping :
#----exchange of variables's values 
#-Swap values without using third value
x=10
y=20
# first sum values 
# x(variable) = x(10) + y(20)
x=x+y  # sum of X and Y is Assigned to X variables
# x=30
# y(variable) = x(30) -y(20)
y=x-y  # y=10
# x(variables) = x(30) - y(20)
x=x-y  #x=20

print (x," ",y)

#<------------------------------------>
# other Method:
a=10
b=20
# simple method 
a,b=b,a
print(a,b)