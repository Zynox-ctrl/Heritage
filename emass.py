from msilib.schema import Error
import smtplib
import os
import sys




print('''                            ,-.                               
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
             `-._,-'   `-._______,-'   `-._,-'                   ''')
print('\nHeritage Email Sender - v1.0.0')


port=587
emaill=input('Your fresh email address: ')
passw=input('Fresh emails password: ')
print('''1> Single Target
2> Mass Target''')
selections=input('Select from Above: ')
if selections == '1':
    target=input('What is the target email: ')
elif selections == '2':
    usernlist=input('Username.txt file: ')
    if os.path.exists(usernlist,):
        usernlist = open(usernlist, 'r')
    else:
        print('File does not exist.')
        sys.exit(1)
    for line in usernlist:
        try:
            target = line.strip('\r\n@outlook.com')
        except:
           print('Failed to read wordlist.') 

    print('Sending to all username list emails.')
print('''1> Gmail
2> Outlook
3> Yahoo
4> By hand''')
servicee=input('Enter a service: ')
if servicee == '1':
    serversmtp = 'smtp.gmail.com'
    port = 465
elif servicee == '2':
    serversmtp = 'smtp-mail.outlook.com'
    port = 587
elif servicee == '3':
    serversmtp = 'smtm.mail.yahoo.com'
    port = 587
elif servicee == '4':
    serversmtp=input('Enter smtp server (Example: smtp.gmail.com : ')
    port=input('Enter the port (Default 587): ')
else:
     print('Error invalid response')


linkk=input('Enter the phishing link: ')
messagee='''Hi there,\nA new login has taken place on this account from a new device on: Friday 13th May : 19:53PM\n If this was you then you do not need to worry about this email. \nHowever if this was not you please take action - ''' + linkk 

smtp = smtplib.SMTP(str(serversmtp), int(port))
smtp.ehlo()
smtp.starttls()


try:
    smtp.login(emaill, passw)
    print('Logged in as ' + emaill +' ' +  passw)
except:
    print(Error)

def send_message():
    if selections == '1':
            try:
                smtp.sendmail(from_addr=emaill, to_addrs=target, msg=messagee)
                print('Sent email to' + target )
            except:
                print('SMTP server busy or invalid server/port')

    elif selections == '2':
        target = line.strip('\r\n') 
        smtp.sendmail(from_addr=emaill, to_addrs=target, msg=messagee) 
        print('Successfully sent an email') 


send_message()