# Random password Generator

import random
import string

pass_len = 8
charvalues = string.ascii_letters + string.digits + string.punctuation
 
#list comprehnsion [function for i in range(n)]
# password = "".join ([random.choice(charvalues) for i in range(pass_len)])

password = ""
for i in range(pass_len):
    password += random.choice(charvalues)

print("your random password is :",password)

