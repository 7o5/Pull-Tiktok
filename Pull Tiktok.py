#KING BERLIN 
import requests
import re
import time
import sys
import sys as n
import time as mm

def slow(M):
 for c in M + '\n':
  n.stdout.write(c)
  n.stdout.flush()
  mm.sleep(1. / 100)
  
berlin = '''[!] Instagram : 680068

  ____            _ _             _______ _ _    _        _    
 |  _ \          | (_)           |__   __(_) |  | |      | |   
 | |_) | ___ _ __| |_ _ __          | |   _| | __ |_ ___ | | __
 |  _ < / _ \ '__| | | '_ \         | |  | | |/ / __/ _ \| |/ /
 | |_) |  __/ |  | | | | | |  _     | |  | |   <| |_ (_) |   <
 |____/ \___|_|  |_|_|_| |_| ( )    |_|  |_|_|\_\\__\___/|_|\_\ o
                             |/                                

                    Coded By | @680068
'''
print(berlin)


print("""
[1] Check One User\n
[2] Check List User
""")

mod = input("[~] Choose Mod :")

if mod == '1':
    username = input('\n[~] Enter Username :')
    url1 = f'https://m.tiktok.com/node/share/user/@{username}'
    headers1 = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'tt_webid_v2=6906543649208567298; tt_webid=6906543649208567298; ttwid=1%7CiHdiehR-DCcEVJlGHclCSaUxHXEdXjqeTKU-qcC5HMU%7C1608661095%7C685ee650b2a4764c2e4ac76e856ed77b488b5178f9696d26240cd8024fcc51df; passport_csrf_token=25d986ab3a12ee63338a796a2d81ff42; store-idc=alisg; tt_csrf_token=NXz1g_bS6jUFV0--CTu1DPlX; odin_tt=416ff172060ae978b3b3cce9da0badbf08d8f44684ae2b8bbd8387c76b6f298c11be34ee8b57bc1db647eaca0b8a9141a0d3228abf3f4e111952613987f2a9cd; cmpl_token=AgQQAPO_F-RO0rAcIaYkJ907xblh6OtRv4DfYPm2rA; sid_guard=764403be8f024eafdc31c3bedf73b9e8%7C1612897457%7C5184000%7CSat%2C+10-Apr-2021+19%3A04%3A17+GMT; uid_tt=f852fb6d44f7feec70333e89255bca3cc738440f9794a5bd693d467c9ecfe42f; uid_tt_ss=f852fb6d44f7feec70333e89255bca3cc738440f9794a5bd693d467c9ecfe42f; sid_tt=764403be8f024eafdc31c3bedf73b9e8; sessionid=764403be8f024eafdc31c3bedf73b9e8; sessionid_ss=764403be8f024eafdc31c3bedf73b9e8; store-country-code=sa; _abck=8350ED4DF75EE990328FC8A9645DAA63~0~YAAQuPkUAtD+0v92AQAAFysuiAVH4bTHE4EdN83xCnAarZxUfcypr1jlN/+gWogSZzlJlRiDXBFDLwwr28wkcOHdhpvbPAICI/pGXLplJopRWo84a1f1zXvRI8iW5nPu6IpKQv6Y8jaiAUVvnaa8hsJ8Ct2JKw/4Co9iINnSDrW66J5101P9W885BzOWi4TjEqLzNiPWJaLn9vpqZhOj0hjeWjZ33PHuf8Of/BjCrx3q34ZE5+/9lh4Hd9tb1fIGMzH1qEWRw6d7ayB61aODSckSpQh3hZgPUeGTmtAX5ZivwSlW7qz7Qf9CsDeK79kE5R4ex7WqWZFOSAyJsOrSSHujNAXHDw==~-1~-1~-1',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not\\A\"Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36'
        }
    req = requests.get(url1, headers=headers1).text
    nice_name = re.findall('"nickname":"(.*?)"', req)
    nice_name2 = "".join(nice_name)
    ch = (nice_name2+'@gmail.com')
    url2 = f"https://mmo69.com/_check_live_email/api.php?email={ch}"
    headers2 = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=mgv0ih4jqqe5sv3p57rkcmgb07; _ga=GA1.2.1110888107.1612952669; _gid=GA1.2.353236417.1612952669',
        'Host': 'mmo69.com',
        'Referer': 'https://mmo69.com/_check_live_email/index.php',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not\\A\"Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
        }
    data2 = {"email":ch}
    rq = requests.get(url2, headers=headers2, data=data2).text
    if rq.find("DIE") >= 0:
        print(f"""
~ This Account Available

~ User : {username}

~ Email : {ch}

----------------------------
""")
        with open('Available @680068.txt', 'a') as x:
            x.write(ch + '\n')
        input(" ")
    else:
        print(f"""

~ This Account Not Available

~ User : {username}

~ Email : {ch}

----------------------------
""")
        input(" ")
elif mod == '2':
    file1 = input("[~] Enter File Name :")
    ff = file1
    file1 = open(ff).read().splitlines()
    for file1 in file1:
        url = f'https://m.tiktok.com/node/share/user/@{file1}'
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'tt_webid_v2=6926024599109109250; tt_webid=6926024599109109250; ttwid=1%7CuU0ZIsyDyN3VZI2n8WRgeKbCOnBi7rzo0O5ubfexN7c%7C1612590836%7C1c5cb49ee5e8f958b35190103ce1ea37891a648dc344853098c36dd9d798f52b; passport_csrf_token=abd11d0de6008199789a3435e8e75597; passport_csrf_token_default=abd11d0de6008199789a3435e8e75597; store-idc=alisg; store-country-code=sa; passport_auth_status=0a5f55489be7d62253f3cc65c0176ba7%2C; passport_auth_status_ss=0a5f55489be7d62253f3cc65c0176ba7%2C; _abck=D86CAAA87344DFBC4EA1879ADDCFE240~0~YAAQ1VEzVg6qVh13AQAAH5vIegVE2Py/9Wi5SskkbJ+qpD4lG65Um+eQ9niI7wVKXxvhaQpyUC+n/TyxeD6zuutte2C687/kacF1AOPIseyP4WV4oN4YZPUsBv96FzzVo6olDgWnVE1yGPN4lIYre6h2gIlQupO94IOfqwFxu20Lupcu5LaVEXCLWi+FdhbUZ3C/Hiwv1VfrF72kg5y4KppxYF7iTRoH0iNyx+rYmtWy3+9YeE/LgViIDqDiE1wHS9IPNP3SX+uSOsZJpUWikgdnnrPBtamwM6sxYqfpJpxf6MzK73vF+mzZDIvU1/Mv0FVKlcZE5yi3lVWE5Yns0n5i9sblKg==~-1~-1~-1; bm_sz=F385086908398A95E604796C237C2E45~YAAQnV4zVu8SpSF3AQAAIDwTgAoCeTewNYm1kYklU/sWL4xNG16wBewKLFLrCUBuXGA1INDc8XyuNqCc13wMRQeX0qjS65m8tZSB9wHiaLgwSAqGyCzQW/LvZJuLzKv8hbsSNWeVYi3xNZum8EOV8LcuAaDxZtaFrodQ+2yZpLJd2QsGyICtWT1xEQj7AWWQ; odin_tt=729d737b073d9823bf2dc7e1cc2f9d283c0f4aade25d6a4db5ca3a4079754abd6485d34b435bb0881bc9aa54181942ae8c7ebc4ec1aeab6296ea72f2de530a37; sid_guard=d4f857d60e8c229cdef498023ab4cf8b%7C1612763228%7C21600%7CMon%2C+08-Feb-2021+11%3A47%3A08+GMT; uid_tt=4ce4df25592d8468f4fe4688775e8cea; uid_tt_ss=4ce4df25592d8468f4fe4688775e8cea; sid_tt=d4f857d60e8c229cdef498023ab4cf8b; sessionid=d4f857d60e8c229cdef498023ab4cf8b; sessionid_ss=d4f857d60e8c229cdef498023ab4cf8b; tt_csrf_token=5rdL0j5zrKEZ-NXoXJlRA9YN',
            'Host': 'm.tiktok.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'non',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
            }
        req = requests.get(url, headers=headers).text
        nice_name = re.findall('"nickname":"(.*?)"', req)
        nice_name2 = "".join(nice_name)
        ch = (nice_name2 + '@gmail.com')
        url2 = f"https://mmo69.com/_check_live_email/api.php?email={ch}"
        headers2 = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'PHPSESSID=mgv0ih4jqqe5sv3p57rkcmgb07; _ga=GA1.2.1110888107.1612952669; _gid=GA1.2.353236417.1612952669',
            'Host': 'mmo69.com',
            'Referer': 'https://mmo69.com/_check_live_email/index.php',
            'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not\\A\"Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
            }
        data2 = {"email":ch}
        rr = requests.get(url2, headers=headers2, data=data2).text
        if rr.find("DIE") >= 0:
            print(f"""

~ This Account As Available

~ User : {file1}

~ Email : {ch}

----------------------------
""")
            with open('Available @680068.txt', 'a') as x:\
                 x.write(ch + '\n')
        else:
            print(f"""

~ This Account Not Available

~ User : {file1}

~ Email : {ch}

----------------------------
""")
   
