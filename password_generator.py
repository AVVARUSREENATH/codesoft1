import random
import string
length=int(input('enter length of passoword: '))
lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbol=string.punctuation
all=lower+upper+symbol+num
password=""
temp=random.sample(all,length)
password="".join(temp)
print(password)