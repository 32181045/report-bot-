
import requests, uuid, secrets

from time import sleep


print("_░▒███████")
print("░██▓▒░░▒▓██")
print("██▓▒░__░▒▓██___██████")
print("██▓▒░____░▓███▓__░▒▓██")
print("██▓▒░___░▓██▓_____░▒▓██")
print("██▓▒░_______________░▒▓██")
print("_██▓▒░______________░▒▓██")
print("__██▓▒░____________░▒▓██")
print("___██▓▒░__________░▒▓██")
print("____██▓▒░________░▒▓██")
print("_____██▓▒░_____░▒▓██")
print("______██▓▒░__░▒▓██")
print("_______█▓▒░░▒▓██")
print("_________░▒▓██")
print("_______░▒▓██")
print("_____░▒▓██")
Print("DONT NOT LOGIN WITH MAIN ACCOUNT")
print("MADE BY 32181045")


uid = uuid.uuid4()

r = requests.Session()

cookie = secrets.token_hex(8) * 2

username = input("your user:")

password = input("your password:")

target = input("target:")

sle = int(input("sleep:"))

print(

    """[1] = spam

[2] = self injury

[3] = hate speech or symbols

[4] =harsement or bulying

[5] = sale or drugs

[6] = violance

[7] = Nudity or pornography

[8] = me ( impreion)"""

)

mode = input("mode?")



def spam():

    global username

    global password

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

        "x-csrftoken": "missing",

        "mid": cookie,

    }

    data = {

        "username": username,

        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:{}".format(password),

        "queryParams": "{}",

        "optIntoOneTap": "false",

    }

    req_login = r.post(url, headers=headers, data=data)

    if ("userId") in req_login.text:

        r.headers.update({"X-CSRFToken": req_login.cookies["csrftoken"]})

        print("login True")

        url_id = "https://www.instagram.com/{}/?__a=1".format(target)

        req_id = r.get(url_id).json()

        user_id = str(req_id["logging_page_id"])

        idd = user_id.split("_")[1]

        done = 1

        while True:

            url_report = "https://www.instagram.com/users/{}/report/".format(idd)

            datas = {"source_name": "", "reason_id": 1, "frx_context": ""}  # spam

            report = r.post(url_report, data=datas)

            print("report done by zubz".format(done))

            sleep(sle)

            done += 1



def self():

    global username

    global password

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

        "x-csrftoken": "missing",

        "mid": cookie,

    }

    data = {

        "username": username,

        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:{}".format(password),

        "queryParams": "{}",

        "optIntoOneTap": "false",

    }

    req_login = r.post(url, headers=headers, data=data)

    if ("userId") in req_login.text:

        r.headers.update({"X-CSRFToken": req_login.cookies["csrftoken"]})

        print("login True")

        url_id = "https://www.instagram.com/{}/?__a=1".format(target)

        req_id = r.get(url_id).json()

        user_id = str(req_id["logging_page_id"])

        idd = user_id.split("_")[1]

        done = 1

        while True:

            url_report = "https://www.instagram.com/users/{}/report/".format(idd)

            datas = {"source_name": "", "reason_id": 2, "frx_context": ""}  # self

            report = r.post(url_report, data=datas)

            print("report done by zubz".format(done))

            sleep(sle)

            done += 1



def hate():

    global username

    global password

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

        "x-csrftoken": "missing",

        "mid": cookie,

    }

    data = {

        "username": username,

        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:{}".format(password),

        "queryParams": "{}",

        "optIntoOneTap": "false",

    }

    req_login = r.post(url, headers=headers, data=data)

    if ("userId") in req_login.text:

        r.headers.update({"X-CSRFToken": req_login.cookies["csrftoken"]})

        print("login True")

        url_id = "https://www.instagram.com/{}/?__a=1".format(target)

        req_id = r.get(url_id).json()

        user_id = str(req_id["logging_page_id"])

        idd = user_id.split("_")[1]

        done = 1

        while True:

            url_report = "https://www.instagram.com/users/{}/report/".format(idd)

            datas = {"source_name": "", "reason_id": 6, "frx_context": ""}  # hate

            report = r.post(url_report, data=datas)

            print("report done by zubz".format(done))

            sleep(sle)

            done += 1



def harsement():

    global username

    global password

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

        "x-csrftoken": "missing",

        "mid": cookie,

    }

    data = {

        "username": username,

        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:{}".format(password),

        "queryParams": "{}",

        "optIntoOneTap": "false",

    }

    req_login = r.post(url, headers=headers, data=data)

    if ("userId") in req_login.text:

        r.headers.update({"X-CSRFToken": req_login.cookies["csrftoken"]})

        print("login True")

        url_id = "https://www.instagram.com/{}/?__a=1".format(target)

        req_id = r.get(url_id).json()

        user_id = str(req_id["logging_page_id"])

        idd = user_id.split("_")[1]

        done = 1

        while True:

            url_report = "https://www.instagram.com/users/{}/report/".format(idd)

            datas = {"source_name": "", "reason_id": 7, "frx_context": ""}  # harsement

            report = r.post(url_report, data=datas)

            print("report done by zubz".format(done))

            sleep(sle)

            done += 1



def Ssleorpromotiondrugs():

    global username

    global password

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

        "x-csrftoken": "missing",

        "mid": cookie,

    }

    data = {

        "username": username,

        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:{}".format(password),

        "queryParams": "{}",

        "optIntoOneTap": "false",

    }

    req_login = r.post(url, headers=headers, data=data)

    if ("userId") in req_login.text:

        r.headers.update({"X-CSRFToken": req_login.cookies["csrftoken"]})

        print("login True")

        url_id = "https://www.instagram.com/{}/?__a=1".format(target)

        req_id = r.get(url_id).json()

        user_id = str(req_id["logging_page_id"])

        idd = user_id.split("_")[1]

        done = 1

        while True:

            url_report = "https://www.instagram.com/users/{}/report/".format(idd)

            datas = {

                "source_name": "",

                "reason_id": 3,

                "frx_context": "",

            }  # Ssleorpromotiondrugs

            report = r.post(url_report, data=datas)

            print("report done by zubz".format(done))

            sleep(sle)

            done += 1



def Violenceorthreatofviolence():

    global username

    global password

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

        "x-csrftoken": "missing",

        "mid": cookie,

    }

    data = {

        "username": username,

        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:{}".format(password),

        "queryParams": "{}",

        "optIntoOneTap": "false",

    }

    req_login = r.post(url, headers=headers, data=data)

    if ("userId") in req_login.text:

        r.headers.update({"X-CSRFToken": req_login.cookies["csrftoken"]})

        print("login True")

        url_id = "https://www.instagram.com/{}/?__a=1".format(target)

        req_id = r.get(url_id).json()

        user_id = str(req_id["logging_page_id"])

        idd = user_id.split("_")[1]

        done = 1

        while True:

            url_report = "https://www.instagram.com/users/{}/report/".format(idd)

            datas = {

                "source_name": "",

                "reason_id": 5,

                "frx_context": "",

            }  # Violenceorthreatofviolence

            report = r.post(url_report, data=datas)

            print("report done by zubz".format(done))

            sleep(sle)

            done += 1



def Nudityorpornography():

    global username

    global password

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

        "x-csrftoken": "missing",

        "mid": cookie,

    }

    data = {

        "username": username,

        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:{}".format(password),

        "queryParams": "{}",

        "optIntoOneTap": "false",

    }

    req_login = r.post(url, headers=headers, data=data)

    if ("userId") in req_login.text:

        r.headers.update({"X-CSRFToken": req_login.cookies["csrftoken"]})

        print("login True")

        url_id = "https://www.instagram.com/{}/?__a=1".format(target)

        req_id = r.get(url_id).json()

        user_id = str(req_id["logging_page_id"])

        idd = user_id.split("_")[1]

        done = 1

        while True:

            url_report = "https://www.instagram.com/users/{}/report/".format(idd)

            datas = {

                "source_name": "",

                "reason_id": 4,

                "frx_context": "",

            }  # Nudityorpornography

            report = r.post(url_report, data=datas)

            print("report done by zubz".format(done))

            sleep(sle)

            done += 1



def mex():

    global username

    global password

    url = "https://www.instagram.com/accounts/login/ajax/"

    headers = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",

        "x-csrftoken": "missing",

        "mid": cookie,

    }

    data = {

        "username": username,

        "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:{}".format(password),

        "queryParams": "{}",

        "optIntoOneTap": "false",

    }

    req_login = r.post(url, headers=headers, data=data)

    if ("userId") in req_login.text:

        r.headers.update({"X-CSRFToken": req_login.cookies["csrftoken"]})

        print("login True")

        url_id = "https://www.instagram.com/{}/?__a=1".format(target)

        req_id = r.get(url_id).json()

        user_id = str(req_id["logging_page_id"])

        idd = user_id.split("_")[1]

        done = 1

        while True:

            url_report = "https://www.instagram.com/users/{}/report/".format(idd)

            datas = {"source_name": "", "reason_id": 8, "frx_context": ""}  # me

            report = r.post(url_report, data=datas)

            print("report done by zubz".format(done))

            sleep(sle)

            done += 1

    else:

        print("login false")

        exit()



if mode == "1":

    spam()

if mode == "2":

    self()

if mode == "3":

    hate()

if mode == "4":

    harsement()

if mode == "5":

    Ssleorpromotiondrugs()

if mode == "6":

    Violenceorthreatofviolence()

if mode == "7":

    Nudityorpornography()

if mode == "8":

    mex()



login()
