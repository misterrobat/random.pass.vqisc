import string
import random
import os
def pass_gen():
    s_l = string.ascii_lowercase
    s_u = string.ascii_uppercase
    s_d = string.digits
    s_p = string.punctuation
    pass_list = []
    pass_list.extend(s_l)
    pass_list.extend(s_u)
    pass_list.extend(s_d)
    pass_list.extend(s_p)
    random.shuffle(pass_list)
    os.system("clear")
    print ("            _          ")
    print ("__   ____ _(_)___  ___ ")
    print ("\ \ / / _` | / __|/ __|")
    print (" \ V / (_| | \__ \ (__ ")
    print ("  \_/ \__, |_|___/\___|")
    print ("         |_|           ")
    pass_length = int(input("Enter Paswword length : "))
    password_resuld = "".join(pass_list[0:pass_length])
    print("Password generated is : ", password_resuld)

pass_gen()    