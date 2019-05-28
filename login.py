import requests
import re
from bs4 import BeautifulSoup
import time



LOGIN_URL = "https://app.keka.com/account/login?returnUrl=/"
USER_EMAIL = ""
USER_PWD = ""

def get_csrf_token(response):
    matches = re.findall(r'name="__RequestVerificationToken"|value="([^ >"]*)"', response)
    # print(filter(matches))
    return matches[1]

def get_value_by_name(name, response):
    html_proc = BeautifulSoup(response, "html.parser")
    result = dict([(element['name'], element['value']) for element in html_proc.find_all('input')])
    return result.get(name, None)

def login(session = requests.Session()):
    response  = session.get(LOGIN_URL, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'Trailers',
    })
    # print(response.text)
    cookies = session.cookies.get_dict()
    data = {
        'SubdomainName': 'myoperator',
        'Email': USER_EMAIL,
        'Password': USER_PWD,
        '__RequestVerificationToken': get_csrf_token(response.text)
    }
    # print(data)
    response = session.post('https://app.keka.com/Account/KekaLogin', headers={
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://app.keka.com/Account/Login?returnurl=/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'Trailers',
    }, cookies=cookies, data=data)
    
    print(response.text)

    if response.status_code >= 200 and response.status_code <= 300:
        time.sleep(3) # Sleep for 3 seconds
        post_login_req = {
            'code': get_value_by_name('code', response.text),
            'id_token': get_value_by_name('id_token', response.text),
            'scope': get_value_by_name('scope', response.text),
            'state': get_value_by_name('state', response.text),
            'session_state': get_value_by_name('session_state', response.text),
        }
        print("Post Login Data:: ", post_login_req)
        post_login_res = session.post('https://myoperator.keka.com/', data=post_login_req)
        print(post_login_res)
        session.get('https://myoperator.keka.com/')

        if post_login_res.status_code >= 200 and post_login_res.status_code <= 300:
            return session, True
    
    return None, False

def logout(session):
    # session.post("")
    print("Logout Success!!")




