#conditional statement
#Conditional statements in Python are used to execute certain blocks of code based on specific conditions. These statements help control the flow of a program, making it behave differently in different situations.
#The primary conditional statements in Python are if, elif, and else.

#if conditional statement
#syntax:
# if(condition):
#  true #this block will execute.
#
#
age = 20
if age>=18:
    print("You are Eligibleto vote")
# short hand if
age = 19
if age >18: print("You are Eigible to vote")

#if else statement:
age = 15
if age <=12:
    print("You can travel for free")
else:
    print("You need to pay for a ticket")

#short hand if-else.
marks = 40
result = "pass" if marks >= 40 else "fail"
print(f"result: {result}")
