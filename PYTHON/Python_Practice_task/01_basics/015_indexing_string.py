# indexing:
# in python indexing start from zero 
# in python string ,array and other variables has consective memory
x="hello"
# positive indexing start zero
print(x[0],x[1]) # result= h e
#negative indexing (start from -1)
print(x[-1],x[-2])   #result = o l

#------Slicing------->
# take a part of string
y = "programming"
# y[slice start , slice end +1]
y_slice= y[3:6+1]
print(y_slice)