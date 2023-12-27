#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q-1 Ans.C)%
6%2


# In[2]:


#Q-2 Ans.B)0
2//3


# In[3]:


#Q-3 Ans.-C)24
6<<2


# In[4]:


#Q-4 Ans-A)2
6&2


# In[9]:


#Q-5 Ans-D)6
6|2


# # Q-6  Ans-C)

# # Q-7  Ans-A)

# # Q-8  Ans-C)

# In[ ]:


#Q-14 Ans:

def findHypotenuse(side1, side2):
    h = (((side1 * side1) + (side2 * side2))**(1/2)); 
    return h; 
  

side1 = 3; 
side2 = 4; 
  
print(findHypotenuse(side1, side2)); 
  


# In[18]:


import math

a = float(input("Enter base: "))
b = float(input("Enter height: "))
x = float(input("Enter angle: "))

c = math.sqrt(a ** 2 + b ** 2)

print("Hypotenuse =", c)


# # Q-9  Ans-A) C)

# # Q-10  Ans-A)

# In[38]:


#Qu-15 Ans.-
string=input("Enter given string= ")
count={}

for letter in string:
    if letter in count:
        count[letter]+=1
    else:
        count[letter]=1
print("Frequency of each charector is..")
for key, value in count.items():
    print(f"{key} occurs {value} times")

    


# In[ ]:


#Qu-11 Ans.
# To take input from the user
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[ ]:


#Qu-12 Ans.
#To take input from the user
num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is composite number")
    else:
        print(num, "is a prime number")


# In[ ]:


#Qu-13 Ans.
string=input("Enter string:")
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")

