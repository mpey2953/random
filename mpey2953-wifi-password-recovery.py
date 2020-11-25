#-------------------------------------------------------------------

#! /usr/local/bin/python3
# coding: utf-8
# author: mpey2953
# date: november 25, 2020
# version: 1.0

# credits: https://nitratine.net/blog/post/get-wifi-passwords-with-python/

#-------------------------------------------------------------------

# import modules and create references
import subprocess
import pyfiglet

# create pyfiglet header
header = pyfiglet.figlet_format("WIFI PASSWORD RECOVERY", font = "digital") 

# print pyfiglet header
print(header) 

# reads known profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')

# splitting string into a list
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# loops through known profiles
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("Network: " + "{:<30}\nPassword: {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))

# prints wifi connection and its password
input("")