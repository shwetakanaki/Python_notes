a=20  # global varible  : the varibale which decalared 
    #  outside the block is called global varible or global scope
    # global varible can be accesed anywhere in the same file and different file
def demo():
    b=90  # local variable: the varibale which decalared 
    # inside the block is called local varible or local scope
    # it can be accessed with in same block where it is initiailsied 
    
    print("local varibale",b)
    print(a)
def demo1():
    print("local varible",b) # cant be accessed 
    
demo()
demo1()




