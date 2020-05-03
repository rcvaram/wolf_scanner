import scanner
import requests
target_url = "https://rcvaram.pythonanywhere.com/"
login_url = "https://rcvaram.pythonanywhere.com/login"
data = {
  'csrf_token': 'IjM5OGEyMDY5YjgyOWNhNTIxYWYwYzAyYWI0ZWI4MTUxZTQzZDMwY2Qi.Xq59tg.lCdZ1KlDaPbJ2tBplX9stJdPrcQ',
  'email': 'admin@gmail.com', 'password': 'admin', 'remember': 'y',
  'submit': 'Log In'
}
res =requests.post(login_url, data =data)
# print(res.content.decode())
links_to_ignore = []
vuln_scanner = scanner.Scanner(target_url, links_to_ignore)
vuln_scanner.session.post(login_url, data)
vuln_scanner.run()