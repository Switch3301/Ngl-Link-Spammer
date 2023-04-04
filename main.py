import httpx
import uuid
import concurrent.futures
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
question = input("Question: ")
namebhai = input("Url: ").replace("https://ngl.link/", "").replace('ngl.link/','').replace('https://','').replace('http://','').replace('/','')


clear()
sent = 0
erorrs = 0
requestss = 0

def title():
    os.system('title  Questions Sent: ' + str(sent) + '  Errors: ' + str(erorrs) + '  Requests: ' + str(requestss))



def GetProxy():
    with open('proxies.txt', "r") as f:
        return random.choice(f.readlines()).strip()
    

def GetFormattedProxy(proxy):
        if '@' in proxy:
            return proxy
        elif len(proxy.split(':')) == 2:
            return proxy
        else:
            if '.' in proxy.split(':')[0]:
                return ':'.join(proxy.split(':')[2:]) + '@' + ':'.join(proxy.split(':')[:2])
            else:
                return ':'.join(proxy.split(':')[:2]) + '@' + ':'.join(proxy.split(':')[2:])




class Main():
    def device_key():
        device_key = uuid.uuid4()
        return device_key
    
    def post(user_name,message):
        global sent, erorrs, requestss
        proxy_str = GetProxy()
        ff_proxy = proxy_str
        proxy_format = GetFormattedProxy(ff_proxy)
        proxy = {"https://": "http://" + proxy_format, "http://": "http://" + proxy_format}
        api = 'https://ngl.link/api/submit'
        device_keyy = Main.device_key()
        payload = f'username={user_name}&question={message}&deviceId={device_keyy}&gameSlug=confessions&referrer='
        content_total = len(payload)
        headers = {
            'authority': 'ngl.link',
            'method': 'POST',
            'path': '/api/submit', 
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.7',
            'content-length': str(content_total),
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://ngl.link',
            'referer': f'https://ngl.link/{user_name}',
            'sec-ch-ua': '"Brave";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
            }

        r = httpx.post(api, headers=headers, data=payload , proxies=proxy, timeout=None)
        requestss += 1
        title()
        if r.status_code == 200:
            print('Successfully sent Question  | ' + str(r.status_code) + " Question ID: "  + str(r.json()['questionId']))
            sent += 1
            title()
        else:
            print('Error - ' + str(r.status_code))
            erorrs += 1
            title()


def post_thread():
    while True:
        try:
            Main.post(namebhai, str(question))
        except Exception as e:
            print(e)

def post_threads():
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(post_thread) for _ in range(100)]
        concurrent.futures.wait(futures)


post_threads()
