# operators 
# Arithmetic: +,-,%,/,*,**
# logical operator: and or not 
# relational: < > <= >= == !=
# bitwise operator : &,|, ! , << ,>> 


a=10
b=2
print("addition",a+b)
print("substraction",a-b)
print("modulus",a%b)  # reminder 
print("divide ",a/b)  # qutiont 
print("multiplication",a*b)
print("exponential",b**a)

# relational operator 

print("a is less than b ",a<b) # false 
print("a is greater than b",a>b) #True
print("a is less than or equls to b",a<=b)# false 
print("a is graeter than or equls to b",a>=b) # true 
print("a is  equls to b",a==b) # false 
print("a is not equls to b",a!=b)# True 

# logical operator
print(a<b and a>b)
     # f      T  --> false 
print(a<b or  a>b)
     # f      T   --> true    
print(not(a<b or  a>b))




# bit wise 
print(a&b)
c=90
print(a&b|c)

print((a|c)&b)

print("left shift",a<<2)
print("right shift",a>>2) 
