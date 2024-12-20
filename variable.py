# initialising the variable 
a=10 
b=90 
print(a,b)
# assigning the multiple variable within single line 
c,d=30,4
print(c)
print(d)


# data type 


a=10 
print(type(a)) 
b='cloud'
print(type(b))
c=1.3
print(type(c))
d=False 
print(type(d))


# Non primitive data types---> if you want to store multiple data in single varible 
#collection
    # 1.list 
    # 2.dict
    # 3.set
    # 4.tuples
    
# list 
# it is collection type 
# it is hetrogeneous 
# duplicate values are allowed or repeataion of the values is allowed 
# it is mutable 
# it is ordered 

# Syntax:  var_name=[value1,value2,value3......]
# ex:
l=[1,2,3,4,'cloud',1.3,True,3,4]
print(l)
l.append(2)  # it is used for to the data at last 
print("after appended=",l)

# to remove the data from list 
l.pop()  # it will remove the data from last 
print("after poping=",l)
l.pop(2) # it will remove the data by using the index 
print("after removing the data using the index value:",l)
l.remove(3) # it will remove the data by using the value 
print("after removing by value 3:",l)
print("lenght of list",len(l))

l.clear()# it is used to remove the multiple data from the list
print(l)
del(l)
print(l)

