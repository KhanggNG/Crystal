import os
import time 
import requests
banner = """
           \x1b[38;5;250m Welcome To Crystal II
        Type [Help] To continue attack
"""
meth = """\x1b[38;5;231mMethods In Tool > home-sky
Methods In Tool > httpspam
Methods In Tool > killer-net
Methods In Tool > skynet"""
def http():
    url = input("\x1b[38;5;231mTargets : ")
    response = requests.get(url)
    status_code = response.status_code
    print(f"\x1b[38;5;231mStatus Server [{url}] Is : [{status_code}]")
def header():
    url = input("\x1b[38;5;231mTargets :")
    response = requests.get(url)

    headers = response.headers
    print("HTTP headers:")
    for header, value in headers.items():
        print(f"{header}: {value}")
help = """\x1b[38;5;231mHTTP > Check Status Server
INFO > Display All Information In Tool
METHODS > Show All Attack Functions In Tool
HEADER > Displaying Full Server Information Using HTTP
ATTACK > Press Attack To Attack"""
def clear():
    os.system("clear")
def getip():
    response = requests.get("https://api.ipify.org/")
    return response.text
def info():
    print("""\x1b[38;5;231mAdmin : [PhuVanDuc]
Vip : [False]
Plan: [Sliver]
My IP : """,getip())
def hethong():
    clear()
    print(banner) 
    while(True):
         cnc = input("\x1b[38;5;231m[\x1b[38;5;231mRoot👻\x1b[38;5;13mCrystal\x1b[38;5;231m] :\x1b[38;5;47m ")
         if cnc == "clear" or cnc == "cls" or cnc == "CLEAR" or cnc == "CLS":
            clear()
         elif cnc == "ATTACK" or cnc == "attack":
            attack()
         elif cnc == "methods" or cnc == "METHODS" or cnc == "method" or cnc == "METHOD":
            print(meth)  
         elif cnc == "HTTP" or cnc == "http":
            http()
         elif cnc == "header" or cnc == "HEADER":
            header()
         elif cnc == "info" or cnc == "INFO":
            info()
         elif cnc == "help" or cnc == "HELP" or cnc == "Help":
            print(help)
         else:
             print("\x1b[38;5;231mInvail Command")

total = "9"
def attack():
    cmc = input("\x1b[38;5;231mMethods> ")
    if "home-sky" in cmc:
       try:
           mth = cmc.split()[0]
           url = input("\x1b[38;5;231mTargets(Domains Supported)> ")
           port = input("\x1b[38;5;231mPorts> ")
           timer = input("\x1b[38;5;231mDuration> ")
           response = requests.get(url)
           status_code = response.status_code
           print(f"\x1b[38;5;250mAttack command has been send to all servers! Your total attack : {total}")
           print(f"\x1b[38;5;250mHost> [{url}]")
           print(f"\x1b[38;5;250mMethods> [{mth}]")
           print(f"\x1b[38;5;250mState before attack>[{status_code}]")
       except IndexError:
           print("Unknow Command")
    elif "skynet" in cmc:
       try:
           mth = cmc.split()[0]
           url = input("\x1b[38;5;231mTargets(Domains Supported> ")
           port = input("\x1b[38;5;231mPorts> ")
           timer = input("\x1b[38;5;231mDuration> ")
           response = requests.get(url)
           status_code = response.status_code
           print(f"\x1b[38;5;250mAttack command has been send to all servers! Your total attack : {total}")
           print(f"\x1b[38;5;250mHost> [{url}]")
           print(f"\x1b[38;5;250mMethods> [{mth}]")
           print(f"\x1b[38;5;250mState before attack>[{status_code}]")
       except IndexError:
           print("Unknow Command")      
    elif "httpspam" in cmc:
       try:
           mth = cmc.split()[0]
           url = input("\x1b[38;5;231mTargets> ")
           port = input("\x1b[38;5;231mPorts> ")
           timer = input("\x1b[38;5;231mDuration> ")
           response = requests.get(url)
           status_code = response.status_code
           print(f"\x1b[38;5;250mAttack command has been send to all servers! Your total attack : {total}")
           print(f"\x1b[38;5;250mHost> [{url}]")
           print(f"\x1b[38;5;250mMethods> [{mth}]")
           print(f"\x1b[38;5;250mState before attack>[{status_code}]")
       except IndexError:
           print("Unknow Command")
    elif "killer-net" in cmc:
       try:
           mth = cmc.split()[0]
           url = input("\x1b[38;5;231mTargets> ")
           port = input("\x1b[38;5;231mPorts> ")
           timer = input("\x1b[38;5;231mDuration> ")
           response = requests.get(url)
           status_code = response.status_code
           print(f"\x1b[38;5;250mAttack command has been send to all servers! Your total attack : {total}")
           print(f"\x1b[38;5;250mHost> [{url}]")
           print(f"\x1b[38;5;250mMethods> [{mth}]")
           print(f"\x1b[38;5;250mState before attack>[{status_code}]")
       except IndexError:
           print("Unknow Command") 
       else:
           print("\x1b[38;5;231mType [methods] for help ")
hethong()                        