import random
str1 = '1234567890'
str2 = 'qwertyuiopasdfghjklzxcvbnm'
str3 = str2.upper()
str4 = str1+str2+str3
ls = list(str4)
random.shuffle(ls)
#Enter the length of the password/Укажите длину пароля
psw = ''.join([random.choice(ls) for x in range(12)])
print(psw)
