import random

alnm='abcdefghijklmnopqrstuvwxyz1234567890@#$%&-+*/!?\(\)\"\':;'
password=""
l=int(input("Enter the length of the password-> "))
#Max length nearly= 4000
#May go above depending on processor and RAM
print("Length is ",l)
for x in list(range(0,l)):
  password+=alnm[random.randint(0,(len(alnm)-1))]
print("\nPassword is ",password)