#Author: Javier Rodríguez.	.havit7.
import sqlite3
import random, string
import sys, os
import subprocess
import uuid
import getpass, os, uuid, hashlib, getmac as gma, requests
from getmac import get_mac_address as macpc
MAC = macpc()
HWID = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
x = "0x" + ''.join(random.choices(string.ascii_letters + string.digits, k=32))

while True:
    print("[1] Create your IdentyThor.")
    print("[2] Login in your IdentyThor.")
    print("[3] Exit.")
    resp = input("Select an option: ")
    if resp == "2":
        print("Your IdentityThor, " + x + ", was created successfully.")
        break
    if resp == "1":
        input("Put ur email: ")
        input("Put ur password: ")
        print("Login successful.")
        print("ACCESS TOKEN: " + x)
        print("MAC: " + MAC)
        print("HWID: " + HWID)
        break
    if resp == "3":
        print("Bye Bye!!!")
        break
