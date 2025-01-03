# swapping 2 numbers with temp variable 
a=10
b=20
print("before swapping",a,b)
temp=a
a=b
b=temp

print("after swapping",a,b)


# swap the 2 numbers without temp varibale 

a=10
b=20
print("before swapping",a,b)
a=a+b  # 30
b=a-b #10
a=a-b #20 
print("after swapping",a,b)