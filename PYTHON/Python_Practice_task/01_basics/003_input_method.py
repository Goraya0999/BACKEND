#-- Input Method :
# ----it is used take input from user end 
#--int(),str(),float()
#----these method is used to specify the input data type because some time program want integer type
#but you type string this give error
name=str(input("Enter Your name:")) #take string
age=int(input("Enter your age:"))
#greeting function:
def greeting(name: str):
    print ("greeting! ",name)
#call a greeting function  
greeting(name)