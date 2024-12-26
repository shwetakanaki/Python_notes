# function: it is set of block of code which will exicute 
            # whenever you call the function 
# 2 types 
    # inbuilt function: append(),pop(),remove() etc
    # user defined:
    #    2 types 
    #      zero parametraised
    #      parametraised 


# syntax:   def fun_name(para1,para2,...):
#               statements     

def demo(): # declartion # zero parametraised function
    a=10    # defination
    b=20
    print("addition",a+b)
    
demo()

def demo1(a,b): # parametraised function 
    print("addition of a and b=",a+b)


demo1(2,5)

# Note : while calling the parametraised function no of arguments 
#      shuld be passed as no of parameter is declared in the Function    


def demo2(a=90,b=None):
    print("demo2()",a,b)


demo2(30,90)




# adavantages 
# code reusability
# it is used to remove the code repeatation


