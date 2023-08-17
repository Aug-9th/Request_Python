import requests

login_url = 'https://qldt.ptit.edu.vn/CMCSoft.IU.Web.Info/Login.aspx'
username = 'B21DCCN499'
password = 'Shyy098'
session = requests.Session()
login_page = session.get(login_url)
login_data = {
    'username': username,
    'password': password
}
r = session.post(login_url, data=login_data)
print(r.status_code)
if r.status_code == 200:
    print("Success!")
else:
    print("Fail!!")
